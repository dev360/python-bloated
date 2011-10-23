
from os.path import join as pjoin, dirname, abspath
import sys

test_root = abspath(dirname(__file__))
lib_path = pjoin(test_root, '..', '..')
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)
