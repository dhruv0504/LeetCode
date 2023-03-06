"""
link: https://leetcode.com/problems/find-peak-element/
status: having a doudt

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""

class Solution(object):
    def findPeakElement(self, nums):
        max = 0
        if len(nums) >= 4:
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    max = i
            for i in range(0,len(nums)-1):
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    if max < i :
                        max = i
        elif len(nums)==3:
            if nums[0] > nums[1] and nums[0] > nums[2]:
                max = 0
            elif nums[1] > nums[0] and nums[1] > nums[2]:
                max = 1
            else:
                max = 2
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                max = 0
            else:
                max=1
        else:
            max= 0
        return max
