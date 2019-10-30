#!/usr/bin/env python
from __future__ import print_function
import unittest
import sys
sys.path.append('../')
from myutils.XbbConfig import XbbConfigReader, XbbConfigTools, XbbConfigChecker

class TestBranchListMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_configs(self):
        configTags = ['Zll2017', 'Zvv2017', 'Wlv2017']
        for configTag in configTags:
            config = XbbConfigTools(config=XbbConfigReader.read('../' + configTag))
            xcc    = XbbConfigChecker(config)
            xcc.checkAll()
            xcc.printErrors()
            self.assertEqual(xcc.getStatus(), 0)

if __name__ == '__main__':
    unittest.main()
