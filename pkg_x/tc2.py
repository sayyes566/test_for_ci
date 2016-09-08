import unittest
import random

class TC2(unittest.TestCase):

    def test_succ2(self):
        pass

    def test_fail2(self):
        self.assertTrue(False)

    def test_fail50(self):
        r = random.randint(1, 100)
        self.assertTrue(r <= 50)


if __name__ == '__main__':
    unittest.main();
