from __future__ import print_function
import os

class FileLocator(object):

    def __init__(self, config=None):
        self.config = config
        try:
            self.xrootdRedirectors = [x.strip() for x in self.config.get('Configuration', 'xrootdRedirectors').split(',') if len(x.strip())>0]
            if len(self.xrootdRedirectors) < 1:
                print("WARNING: empty list of xrootd redirectors given!")
        except Exception as e:
            if config:
                print (e)
                print("WARNING: no xrootd redirector given!")
            self.xrootdRedirectors = None
        try:
            self.pnfsStoragePath = self.config.get('Configuration', 'pnfsStoragePath').strip()
        except:
            if config:
                print("WARNING: no pnfs storage path given!")
            self.pnfsStoragePath = None

        self.storagePathPrefix = '/store/'
        self.pnfsPrefix = '/pnfs/'

    # check if path is relative to /store/
    def isStoragePath(self, path):
        return path.startswith(self.storagePathPrefix)

    # check if a path is a PNFS directory (with or without redirector)
    def isPnfs(self, path):
        return self.pnfsPrefix in path

    def getDeletionCommand(self, fileName):
        localName = self.getLocalFileName(fileName)
        if ('/' + localName.strip().strip('/')).startswith(self.pnfsPrefix):
            if self.xrootdRedirectors and len(self.xrootdRedirectors) > 0:
                serverName = self.xrootdRedirectors[0].split('root://')[1].split(':')[0]
                return "xrdfs {server} rm {file}".format(server=serverName, file=localName)
            else:
                raise Exception("NoRedirectorSpecified")
        else:
            return "rm {file}".format(file=localName)
    
    def getMakedirCommand(self, fileName):
        localName = self.getLocalFileName(fileName)
        if ('/' + localName.strip().strip('/')).startswith(self.pnfsPrefix):
            if self.xrootdRedirectors and len(self.xrootdRedirectors) > 0:
                serverName = self.xrootdRedirectors[0].split('root://')[1].split(':')[0]
                return "xrdfs {server} mkdir {file}".format(server=serverName, file=localName)
            else:
                raise Exception("NoRedirectorSpecified")
        else:
            return "mkdir {file}".format(file=localName)

    def fileExists(self, fileName):
        return os.path.isfile(self.getLocalFileName(fileName))

    def directoryExists(self, fileName):
        return os.path.isdir(self.getLocalFileName(fileName))

    # ------------------------------------------------------------------------------
    # get file name WITH redirector
    # ------------------------------------------------------------------------------
    def getXrootdFileName(self, rawFileName):
        xrootdFileName = rawFileName.strip()
        if self.isStoragePath(xrootdFileName):
            xrootdFileName = self.pnfsStoragePath + xrootdFileName.strip()
        if self.isPnfs(xrootdFileName):
            # replace already existing redirectors with primary one
            if self.xrootdRedirectors:
                for redirector in self.xrootdRedirectors:
                    xrootdFileName = xrootdFileName.replace(redirector, '')
                xrootdFileName = self.xrootdRedirectors[0] + xrootdFileName
            return xrootdFileName.strip()
        else:
            return xrootdFileName.strip()

    # ------------------------------------------------------------------------------
    # get file name WITHOUT redirector, but with complete PNFS path in case of a 
    # /store/ path.
    # ------------------------------------------------------------------------------
    def getLocalFileName(self, rawFileName):
        if rawFileName:
            localFileName = rawFileName.strip()
            if self.xrootdRedirectors:
                for redirector in self.xrootdRedirectors:
                    localFileName = localFileName.replace(redirector, '')
            if localFileName.startswith('/store/'):
                localFileName = self.pnfsStoragePath + localFileName.strip()
            return localFileName
        else:
            print ("\x1b[31mERROR: invalid file name\x1b[0m")
            raise Exception("InvalidFileName")

