import os
import sys
parent_rpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(parent_rpath))
import roatools  # noqa


def test_module_exists():
    assert 'roatools' in sys.modules


def test_import():
    x = roatools.TestClass()
    assert x.test() == 'Hello'
