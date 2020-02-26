#!/usr/bin/env python
from __future__ import print_function
import unittest
import sys
sys.path.append('../')
from myutils.XbbConfig import XbbConfigReader, XbbConfigTools, XbbConfigChecker

class TestBranchListMethods(unittest.TestCase):

    def setUp(self):
        self.statusDict = {}
        self.configTags = []
        with open("../configs.dat", "r") as fp1:
            for line in fp1:
                self.configTags.append(line.strip())
        print(self.configTags)
        self.statusDict = {k: -1 for k in self.configTags}

    def test_configs(self):
        for configTag in self.configTags:
            config = XbbConfigTools(config=XbbConfigReader.read('../' + configTag))
            xcc    = XbbConfigChecker(config)
            xcc.checkAll()
            xcc.printErrors()
            status = xcc.getStatus()
            print("STATUS:", configTag, "=>", status)
            self.assertEqual(status, 0)
            self.statusDict[configTag] = status

    def tearDown(self):
        print("STATUS:")
        for k in sorted(self.statusDict.keys()):
            if self.statusDict[k] != 0:
                print("\x1b[31m >", k, self.statusDict[k], " (ERROR)\x1b[0m")
            else:
                print(" >", k, self.statusDict[k], "(OK)")

if __name__ == '__main__':
    unittest.main()
