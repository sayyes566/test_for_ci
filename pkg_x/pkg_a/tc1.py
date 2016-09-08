import unittest

class TC1(unittest.TestCase):

    def test_succ1(self):
        pass

    def test_fail1(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main();
