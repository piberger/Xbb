#!/usr/bin/env python
from __future__ import print_function
import json
import re

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

