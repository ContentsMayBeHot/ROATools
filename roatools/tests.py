import unittest
import sys

import roaparse


class TestROAParse(unittest.TestCase):
    # TODO: Create tests for ROAParse
    def test_imported(self):
        self.assertTrue("roaparse" in sys.modules)


class TestROAManager(unittest.TestCase):
    # TODO: Create tests for ROAParse
    def test_imported(self):
        self.assertTrue("roamanager" in sys.modules)


class TestROASync(unittest.TestCase):
    # TODO: Create tests for ROAParse
    def test_imported(self):
        self.assertTrue("roasync" in sys.modules)


if __name__ == "__main__":
    unittest.main()
