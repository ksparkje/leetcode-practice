# 673. Number of Longest Increasing Subsequence
# Medium
#
# Given an unsorted array of integers, find the number of longest increasing subsequence.
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
# Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

from typing import List
from functools import reduce

class Solution:
    def findNumberOfLIS(self, A: List[int]) -> int:

        if not A:
            return 0

        counts = [1] * len(A)
        number_of_path = [1] * len(A)

        for i, item in enumerate(A[1:], 1):
            max_so_far = counts[i]
            num_path = 0
            for j, prev_item in enumerate(A[:i]):
                if prev_item < item:
                    max_so_far = max(max_so_far, counts[j] + 1)
            for j, prev_item in enumerate(A[:i]):
                if prev_item < item and (counts[j] + 1 == max_so_far):
                    num_path += number_of_path[j]
            counts[i] = max_so_far
            number_of_path[i] = max(num_path, number_of_path[i])

        max_counts = max(counts)
        max_counts_path = [number_of_path[i] for i in range(len(A)) if counts[i] == max_counts]

        return sum(max_counts_path)


