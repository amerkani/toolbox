# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from toolbox.plotting import plot_trace


class TestSimple(unittest.TestCase):
    def test_add_one(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
