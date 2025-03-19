# Vacation Planning

You are planning a road trip and would like to figure out which contiguous days you can cover a target number of miles. Given a list of `miles` where `miles[i]` is the number of miles you can cover on the `ith` day and a `target` number of miles you are trying to reach, write a function that will return the minimum number of days you can drive while still covering the `target` number of miles. If no such solution exists, return `0`.

## **Example 1:**
```
Input: target = 7, miles = [2,3,1,2,5,1]
Output: 2
Explanation: The shortest number of contiguous days where we can reach 7 miles is 2 (days from index 3 to 4).
```

## **Example 1:**
```
Input: target = 3, miles = [1,4,5]
Output: 1
Explanation: We can reach the target with a single day (days at index 1 or 2).
```