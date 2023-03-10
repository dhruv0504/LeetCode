"""
link: https://leetcode.com/problems/powx-n/
ans-link: https://colab.research.google.com/drive/1qjBKBTQAFtoq4btKow58_lINp-9NOcKB#scrollTo=jJ4zhzFmCxdz

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
-104 <= xn <= 104
"""

n= 2.00000
p = -2
ans = 1

if p > 0:
  for i in range(p):
    ans*=n 
elif p < 0:
  for i in range(-p):
    ans/=n
else:
  ans=1

print('%.5f' % ans) 