import unittest
from GithubAPI567 import githubAPI
from unittest import mock
from unittest.mock import MagicMock

class TestGithubAPI567(unittest.TestCase):
    @mock.patch('GithubAPI567.githubAPI')
    def testWorkingUserInputMock(self,mockrequirements):
        mockrequirements.return_value.json.return_value= ('mfahim5')
        res=githubAPI("mfahim5")
        self.assertEqual(res, True)
    
    # def testWorkingUserInputMock1(self,mockrequirements):
    #     mockrequirements.return_value.status_code= ('Repo Name: Complexity    Number of commits: 30 Repo Name: Final_Project_SW555   Number of commits: 30 Repo Name: FocusBot      Number of commits: 8 Repo Name: Hoboken-Happening     Number of commits: 1 Repo Name: Personal-Website      Number of commits: 7 Repo Name: SSW-345       Number of commits: 28 Repo Name: SSW567-HW4a   Number of commits: 26 Repo Name: test-HW4-345  Number of commits: 2 Repo Name: test-SSW-345  Number of commits: 2 Repo Name: TriangleTest  Number of commits: 12')
    #     res=githubAPI("mfahim5")
    #     self.assertEqual(res, 'Repo Name: Complexity    Number of commits: 30 Repo Name: Final_Project_SW555   Number of commits: 30 Repo Name: FocusBot      Number of commits: 8 Repo Name: Hoboken-Happening     Number of commits: 1 Repo Name: Personal-Website      Number of commits: 7 Repo Name: SSW-345       Number of commits: 28 Repo Name: SSW567-HW4a   Number of commits: 26 Repo Name: test-HW4-345  Number of commits: 2 Repo Name: test-SSW-345  Number of commits: 2 Repo Name: TriangleTest  Number of commits: 12' )
    def testNonWorkingUserInputMock1(self):
        self.assertEqual(githubAPI(000), 'Github account must be written correctly', 'Strings are only allowed in githubAPI')   
#     def testNonWorkingUserInputMock2(self):
#         self.assertEqual(githubAPI("HIII"), False)

    def testNonWorkingUserInputMock3(self):
        self.assertEqual(githubAPI(9999), 'Github account must be written correctly', 'Strings are only allowed in githubAPI')       

if __name__ =="__main__":
    print('Testing all the cases')
    unittest.main()
