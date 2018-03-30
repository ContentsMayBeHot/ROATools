import os, sys
parent_rpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(parent_rpath))
import roa


def test_module_exists():
    assert 'roa' in sys.modules


def test_import():
    x = roa.TestClass()
    assert x.test() == 'Hello'
