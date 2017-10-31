#!/usr/bin/env python
from __future__ import print_function
import unittest
import sys
sys.path.append('../')
from myutils.FileList import FileList

class TestBranchListMethods(unittest.TestCase):

    def setUp(self):
        self.fileList = [
            '/some/long/path/to/file/blablablablablablablablablablablablabla/file_1.root',
            '/some/long/path/to/file/blablablablablablablablablablablablabla/file_2.root',
            '/some/long/path/to/file/blablablablablablablablablablablablabla/file_3.root',
            '/some/long/path/to/file/blablablablablablablablablablablablabla/file_4.root',
            '/some/long/path/to/file/blablablablablablablablablablablablabla/file_5.root',
            '/some/long/path/to/file/blablablablablablablablablablablablabla/file_6.root',
        ]

    def test_FileList(self):
        compressedFileList = FileList.compress(self.fileList)
        decompressedFileList = FileList.decompress(compressedFileList)
        print('uncompressed length:',len(';'.join(self.fileList)))
        print('compressed length:',len(compressedFileList))
        self.assertEqual(self.fileList, decompressedFileList)

    def test_FileListDamaged(self):
        compressedFileList = FileList.compress(self.fileList)
        # corrupt the file list by removing the last character
        compressedFileList = compressedFileList[:-1]
        with self.assertRaises(Exception) as e:
            decompressedFileList = FileList.decompress(compressedFileList)

    def test_FileListDamaged2(self):
        compressedFileList = FileList.compress(self.fileList)
        # corrupt the file list
        compressedFileList = 'H'+compressedFileList[1:]
        with self.assertRaises(Exception) as e:
            decompressedFileList = FileList.decompress(compressedFileList)

    def test_FileListEmpty(self):
        print('empty:',FileList.compress([]))
        # corrupt the file list
        compressedFileList = 'base64:'
        with self.assertRaises(Exception) as e:
            decompressedFileList = FileList.decompress(compressedFileList)


if __name__ == '__main__':
    unittest.main()
