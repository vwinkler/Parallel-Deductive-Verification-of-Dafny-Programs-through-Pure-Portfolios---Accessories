import unittest
import shlex


class ShlexTest(unittest.TestCase):
    def test_double_quoted_token(self):
        self.assertEqual(["this", "is", "a test"], shlex.split('this is "a test"'))

    def test_single_quoted_token(self):
        self.assertEqual(["this", "is", "a test"], shlex.split("this is 'a test'"))


if __name__ == '__main__':
    unittest.main()
