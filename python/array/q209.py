# 209. Minimum Size Subarray Sum
# Medium
#
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.
#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which
# the time complexity is O(n log n).
from collections import deque
from itertools import accumulate
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_length = impossible = len(nums) + 1
        p = accumulate([0] + nums)
        monoq = deque()

        for idx, py in enumerate(p):
            while monoq and py - monoq[0][1] >= s:
                min_length = min(min_length, idx - monoq.popleft()[0])

            monoq.append([idx, py])

        return min_length if min_length != impossible else 0



