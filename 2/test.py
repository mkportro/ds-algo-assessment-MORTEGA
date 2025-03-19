import unittest
from problem import Solution

isValidSudoku = Solution.isValidSudoku

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(isValidSudoku(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    def test_case_1(self):
        self.run_test([[["5","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]], True)
    
    def test_case_2(self):
        self.run_test([[["8","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]], False)
        
    def test_case_3(self):
        self.run_test([[[".",".",".",".","5",".",".","1","."]
                         ,[".","4",".","3",".",".",".",".","."]
                         ,[".",".",".",".",".","3",".",".","1"]
                         ,["8",".",".",".",".",".",".","2","."]
                         ,[".",".","2",".","7",".",".",".","."]
                         ,[".","1","5",".",".",".",".",".","."]
                         ,[".",".",".",".",".","2",".",".","."]
                         ,[".","2",".","9",".",".",".",".","."]
                         ,[".",".","4",".",".",".",".",".","."]]], False)

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{self._testMethodName} FAILED")
        else:
            print(f"{self._testMethodName} PASSED")


if __name__ == '__main__':
    unittest.main()