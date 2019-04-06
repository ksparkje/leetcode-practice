# 974. Subarray Sums Divisible by K
#
# Given an array A of integers, return the number of (contiguous, non-empty)
# subarrays that have a sum divisible by K.
#
# Example 1:
#
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
from itertools import accumulate
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        mod_counts = [1] + [0] * (K - 1)
        sum_so_far = 0
        number_of_sub = 0
        for idx, elem in enumerate(A):
            sum_so_far = (sum_so_far + elem) % K
            number_of_sub += mod_counts[sum_so_far]
            mod_counts[sum_so_far] += 1
        return number_of_sub


if __name__ == '__main__':
    A = [4, 5, 0, -2, -3, 1]
    s = Solution()
    print(s.subarraysDivByK(A, 5))

