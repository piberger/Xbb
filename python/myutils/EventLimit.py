#!/usr/bin/env python
from BranchTools import AddCollectionsModule

class EventLimit(AddCollectionsModule):

    def __init__(self, limit): 
        self.limit = limit
        self.counter = 0
        super(EventLimit, self).__init__()

    def customInit(self, initVars):
        pass
    
    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)

            self.counter += 1
            if self.counter > self.limit:
                return False

