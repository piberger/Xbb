#!/usr/bin/env python
from __future__ import print_function
import unittest
import os
import glob

class TestClean(unittest.TestCase):

    def test_Clean(self):
        fileNames = glob.glob('tree_*.root')
        for fileName in fileNames:
            print("remove ", fileName)
            os.remove(fileName)
        fileNamesAfter = glob.glob('tree_*.root')
        self.assertEqual(len(fileNamesAfter), 0)

if __name__ == '__main__':
    unittest.main()
