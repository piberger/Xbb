#!/usr/bin/env python
from __future__ import print_function
import json

class XbbTools(object):

    @staticmethod
    def readJson(fileName):
        with open(fileName, 'r') as fp:
            res = json.load(fp)
        return res
            

