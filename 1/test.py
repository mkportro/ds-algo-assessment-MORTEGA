import unittest
from problem import Solution

planVacation = Solution.planVacation

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(planVacation(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    def test_case_1(self):
        self.run_test([[2,3,1,2,5,1],7], 2)
    
    def test_case_2(self):
        self.run_test([[1,4,5],3], 1)
        

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{self._testMethodName} FAILED")
        else:
            print(f"{self._testMethodName} PASSED")


if __name__ == '__main__':
    unittest.main()