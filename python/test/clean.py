#!/usr/bin/env python
from __future__ import print_function
import unittest
import os
import glob
import shutil

class TestClean(unittest.TestCase):

    def test_Clean(self):
        scratchDirectory = os.environ['SCRATCH_DIR'] if 'SCRATCH_DIR' in os.environ else '.'
        fileNames = glob.glob(scratchDirectory + '/tree_*.root')
        for fileName in fileNames:
            print("remove ", fileName)
            os.remove(fileName)
        fileNamesAfter = glob.glob(scratchDirectory + '/tree_*.root')
        self.assertEqual(len(fileNamesAfter), 0)
        shutil.rmtree(scratchDirectory + '/tmp/')
        shutil.rmtree(scratchDirectory + '/cache/')

if __name__ == '__main__':
    unittest.main()
