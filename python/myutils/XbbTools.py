#!/usr/bin/env python
from __future__ import print_function
import json
import re
import fnmatch

class XbbTools(object):

    @staticmethod
    def readJson(fileName):
        with open(fileName, 'r') as fp:
            res = json.load(fp)
        return res

    @staticmethod
    def splitParts(s):
        p_raw = [x for x in re.split('([+\-=/*,\(\)><^\|\&\!])', s) if len(x) > 0]
        p     = []
        ac    = []
        for x in p_raw:
            ac.append(x)
            t = ''.join(ac)
            if t.count('[')==t.count(']'):
                p.append(t)
                ac=[]
        if len(ac) > 0:
            raise Exception("UnbalancedBrackets")
        return p

    @staticmethod
    def joinParts(p):
        return ''.join(p)

    @staticmethod
    def parseReplacementRules(replacementRulesList):
        return [ x.split('>') for x in replacementRulesList ]

    @staticmethod
    def applyReplacementRules(nominalVariable, replacementRules):
        result = nominalVariable
        replacements = []
        # replace all matching parts by placeholders first to avoid multiple replacements of a single expression
        for x in replacementRules:
            placeholder = "###%d###"%len(replacements)
            newResult = result.replace(x[0], placeholder)
            if newResult != result:
                replacements.append([placeholder, x[1]])
                result = newResult
        # fill the placeholders
        for replacement in replacements:
            result = result.replace(replacement[0], replacement[1])
        return result

    @staticmethod
    def getSystematicsVariationTemplate(nominalVariable, replacementsList):
        stringParts         = XbbTools.splitParts(nominalVariable)
        replacementRules    = XbbTools.parseReplacementRules(replacementsList)
        replacedStringParts = [XbbTools.applyReplacementRules(x, replacementRules) for x in stringParts]
        replacedVariable    = XbbTools.joinParts(replacedStringParts)
        return replacedVariable

    @staticmethod
    def getReplacementRulesList(config, syst):
        replacementRulesDict = eval(config.get('LimitGeneral', 'sys_cut_suffix'))
        return replacementRulesDict[syst] if isinstance(replacementRulesDict[syst], list) else [replacementRulesDict[syst]]

    @staticmethod
    def filterSampleList(sampleIdentifiers, samplesList):
        if samplesList and len([x for x in samplesList if x]) > 0:
            filteredList = []
            for expr in samplesList:
                if expr in sampleIdentifiers:
                    filteredList.append(expr)
                elif '*' in expr:
                    for sampleIdentifier in sampleIdentifiers:
                        if fnmatch.fnmatch(sampleIdentifier, expr):
                            filteredList.append(sampleIdentifier)
            filteredList = list(set(filteredList))
            return filteredList
        else:
            return sampleIdentifiers

    @staticmethod
    def parseSamplesList(samplesListString):
        return XbbTools.parseList(samplesListString, separator=',')

    @staticmethod
    def parseList(listString, separator=' '):
        return [x.strip() for x in listString.strip().split(separator) if len(x.strip()) > 0]

    @staticmethod
    def getSampleTreeFileNames(pathIN, folderName):
        filenames = open(pathIN+'/'+folderName+'.txt').readlines()

        ## search the folder containing the input files
        inputFiles = []

        for filename_ in filenames:
            if '.root' in filename_ :
                inputFiles.append(filename_.rstrip('\n'))

        return inputFiles

    @staticmethod
    def splitSystVariation(syst, sample=None):
        if syst.lower() == 'nominal' or (sample is not None and sample.isData()):
            systBase = None
            UD = None
        else:
            systBase = '_'.join(syst.split('_')[:-1])
            UD = syst.split('_')[-1]
        return systBase, UD

    @staticmethod
    def sanitizeExpression(expression, config, debug=False):
        if config.has_option('General', 'sanitizeExpression'):
            rules = eval(config.get('General', 'sanitizeExpression'))
            newExpression = expression
            for rule in rules:
                newExpression = newExpression.replace(rule[0], rule[1])
            if debug and newExpression != expression:
                print("DEBUG: sanitized expression:")
                print("DEBUG: from:", expression)
                print("DEBUG:   to:", newExpression)
            return newExpression
        else:
            return expression

    @staticmethod
    def getMvaSystematics(mvaName, config):
        return XbbTools.parseList(config.get(mvaName, 'systematics') if (config.has_section(mvaName) and config.has_option(mvaName, 'systematics')) else config.get('systematics', 'systematics'), separator=' ')

class XbbMvaInputsList(object):

    def __init__(self, expressions, config=None):
        self.config = config
        self.expressions = expressions

    def get(self, i, syst=None, UD=None):
        nominal = self.expressions[i]
        if syst is None:
            return nominal
        else:
            replacementRulesList = XbbTools.getReplacementRulesList(self.config, syst)
            sysVar = XbbTools.getSystematicsVariationTemplate(nominal, replacementRulesList)
            sysVar = sysVar.replace('{syst}', syst).replace('{UD}', UD)
            return sysVar

    def length(self):
        return len(self.expressions)
