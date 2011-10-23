"""Force import of all modules in this package in order to get the standard test runner to pick up the tests. """
import os
from os.path import join as pjoin, dirname, abspath
import sys

test_root = abspath(dirname(__file__))
lib_path = pjoin(test_root, '..', '..')
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

modules = [filename.rsplit('.', 1)[0]
           for filename in os.listdir(os.path.dirname(__file__))
           if filename.endswith('.py') and not filename.startswith('_')]
__test__ = dict()

for module in modules:
    exec("from bloated.tests.%s import __doc__ as module_doc" % module)
    exec("from bloated.tests.%s import *" % module)

    __test__[module] = module_doc or ""

import unittest

unittest.main()
