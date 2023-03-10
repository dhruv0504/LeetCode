"""
link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
ans-link: https://colab.research.google.com/drive/1Pa0tH7GSe1Xyki1A91ALPLibC5I_gxU4#scrollTo=i8Pk2zRv6u1P

Given the head of a linked list, remove the nth node from the end of the list and return its head. 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

head = [1,2,3,4,5]
n=1

for i in range(len(head)-n,len(head)-1):
  head[i] = head[i+1]

print(head[:len(head)-1])