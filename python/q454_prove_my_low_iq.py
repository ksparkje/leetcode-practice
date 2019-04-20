# 454. 4Sum II
# Medium
#
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
# there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
# All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
#
# Example:
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
from typing import List
from collections import Counter


'''
liuwenqing657
January 9, 2019 11:03 AM

I feel my IQ is screwed like a shit by your answer
'''
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter = Counter(a + b for a in A for b in B)
        return sum(counter[-(c + d)] for c in C for d in D)

if __name__ == '__main__':
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    s = Solution()
    print(s.fourSumCount(A, B, C, D))













































