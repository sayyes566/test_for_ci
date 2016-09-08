import unittest

class TopLevelTC(unittest.TestCase):

    def test_succ(self):
        pass

    def test_fail(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main();
