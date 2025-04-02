from operator import length_hint
import sys
class Solution:
    def planVacation(self, miles, target):
        # Time complexity: 
        # Space complexity:
        
        # Remove pass and write code here
        min_days = sys.maxsize
        daysCount = 0
        current_miles = 0
        left = 0

        #                     0 1 2 3 4 5
        #target = 7, miles = [2,3,1,2,5,1]
        #output: 2

        for right in range(len(miles)): #advance right ptr
            current_miles += miles[right]

            while current_miles >= target: #advance left ptr to shrink window
                daysCount = right + 1
                min_days = min(min_days, daysCount)

                current_miles -= miles[left]
                left += 1

'''
PROBLEM
figure out which contiguous days you can cover a target number of miles
miles[i] = number of miles you can cover on the ith day
target = number of miles you are trying to reach
return -> minimum number of days you can drive while still covering the `target` number of miles
if no such solution exists, return `0`


EXAMPLES
Input: target = 7, miles = [2,3,1,2,5,1]
Output: 2
Explanation: The shortest number of contiguous days where we can reach 7 miles is 2 (days from index 3 to 4).

Input: target = 3, miles = [1,4,5]
Output: 1
Explanation: We can reach the target with a single day (days at index 1 or 2).

CONSTRAINTS
1 <= target <= 10^9
1 <= miles.length <= 10^5
1 <= miles[i] <= 10^4
'''

'''
SOLUTION PSUEDOCODE

sliding window...
left and right pointer
left stays, right iterates
    add each value together to reach target
    
    when target reached, advance left pointer to close window
        subtract left value from current miles
        check value against target
        advance left ptr

    advance right pointer, repeat above steps

'''