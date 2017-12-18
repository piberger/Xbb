#!/usr/bin/env python
from __future__ import print_function
from myutils import BetterConfigParser
import sys
import difflib
import os

def diffConfigFile(tag1, tag2, fileName):
    print("file:", fileName)
    config1 = BetterConfigParser()
    config2 = BetterConfigParser()
    config1.read(tag1 + 'config/' + fileName)
    config2.read(tag2 + 'config/' + fileName)

    sections = list(set(config1.sections() + config2.sections()))
    commonSections = [x for x in sections if x in config1.sections() and x in config2.sections()]
    print("common sections:", commonSections)

    for section in commonSections:
        firstItemInSection = True

        items1d = {x[0]:x[1] for x in config1.items(section, raw=True)}
        items2d = {x[0]:x[1] for x in config2.items(section, raw=True)}
        items1 = [x[0] for x in config1.items(section, raw=True)]
        items2 = [x[0] for x in config2.items(section, raw=True)]
        items = list(set(items1 + items2))
        commonItems = list(set([x for x in items if x in items1 and x in items2]))

        for item in commonItems:
            if item not in os.environ:
                try:
                    item1 = config1.get(section, item)
                    item2 = config2.get(section, item)
                    item1 = items1d[item]
                    item2 = items2d[item]
                    if item1 != item2:
                        if firstItemInSection:
                            firstItemInSection = False
                            print('-'*80)
                            print(' \x1b[34m' + fileName + '\x1b[0m: ' + section)
                            print('-'*80)
                        print(section + ':' + item)
                        d = difflib.Differ()
                        result = list(d.compare([item1], [item2]))
                        for line in result:
                            if line.startswith('+'):
                                color = '\x1b[31m'
                            elif line.startswith('-'):
                                color = '\x1b[32m'
                            elif line.startswith('?'):
                                color = '\x1b[34m'
                            print('  '+color+line+'\x1b[0m')

                except Exception as e:
                    pass
                    #print("EXCEPTION:", e)

configTag1 = sys.argv[1]
configTag2 = sys.argv[2]

configFiles = 'paths.ini general.ini cuts.ini training.ini datacards.ini plots.ini lhe_weights.ini samples_nosplit.ini'.split(' ')

for configFile in configFiles:
    diffConfigFile(configTag1, configTag2, configFile)
