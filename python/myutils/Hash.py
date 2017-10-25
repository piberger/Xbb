from __future__ import print_function
import hashlib

class Hash(object):

    def __init__(self, sample, minCut = '1', subCut = None, branches = None, splitFiles = -1, debug = False):
        
        # basic cut(+part) hash
        self.hashKey = '%s_%s' % (sample, minCut)
        if splitFiles > 0:
            self.hashKey += '_split%d' % (splitFiles)
        self.hash = hashlib.sha224(self.hashKey).hexdigest()

        # including subcut
        if subCut:
            if debug:
                print ('hash function debug:')
                print (' > \x1b[32mKEY:', self.hashKey, '\x1b[0m')
            self.hashKey = '%s_[%s]' % (self.hash, subCut)
            self.hash = hashlib.sha224(self.hashKey).hexdigest()

        # including branchnames
        if branches:
            if debug:
                print ('hash function debug:')
                print (' > \x1b[32mKEY:', self.hashKey, '\x1b[0m')
            branchNames = ','.join(sorted(branches))
            self.hashKey = '%s_<%s>' % (self.hash, branchNames)
            self.hash = hashlib.sha224(self.hashKey).hexdigest()

        if debug:
            print ('hash function debug:')
            print (' > \x1b[32mKEY:', self.hashKey, '\x1b[0m')
            print (' > \x1b[33mHASH:', self.hash, '\x1b[0m')


    def get(self):
        return self.hash
