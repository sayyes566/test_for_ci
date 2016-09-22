import unittest

class TC1(unittest.TestCase):

    def test_succ1(self):
        '''This test case always passes
        '''
        pass

    def test_fail1(self):
        '''This test case always fails
        '''
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main();
