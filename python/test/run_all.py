#!/usr/bin/env python
from __future__ import print_function
import unittest

loader = unittest.TestLoader()
loader.testMethodPrefix = "test"
suite1 = loader.discover('.', pattern="init.py")
suite2 = loader.discover('.', pattern="test_*.py")
suite3 = loader.discover('.', pattern="clean.py")
alltests = unittest.TestSuite((suite1, suite2, suite3))
unittest.TextTestRunner(verbosity=2).run(alltests)
