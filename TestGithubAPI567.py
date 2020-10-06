import unittest
from GithubAPI567 import githubAPI
from unittest import mock

class TestGithubAPI567(unittest.TestCase):
    def testWorkingUserInput(self):
        self.assertEqual(githubAPI('mfahim5'), True)
    
    def testNonWorkingUserInput1(self):
        self.assertEqual(githubAPI(000), 'Github account must be written correctly', 'Strings are only allowed in githubAPI')   
    def testNonWorkingUserInput2(self):
        self.assertEqual(githubAPI("HIIIII"), False)
    def testNonWorkingUserInput3(self):
        self.assertEqual(githubAPI(11), 'Github account must be written correctly', 'Strings are only allowed in githubAPI')  
    def testNonWorkingUserInput4(self):
        self.assertEqual(githubAPI(9999), 'Github account must be written correctly', 'Strings are only allowed in githubAPI')       

if __name__ =="__main__":
    print('Testing all the cases')
    unittest.main()