import unittest

class TopLevelTC(unittest.TestCase):

    def test_succ(self):
        '''A very important test case!
        '''
        pass

    def test_fail(self):
        '''Author: Nobody
        '''
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main();
