"""
link: https://leetcode.com/problems/intersection-of-two-arrays/

349. Intersection of Two Arrays
Easy
4.4K
2.1K
Companies
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
list1 = [4,9,5]
list2 = [9,4,9,8,4]
list = []

for i in list1:
    for j in list2:
        if i==j:
            if i not in list:
                list.append(i) 

print(list)