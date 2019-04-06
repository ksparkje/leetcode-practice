# 560. Subarray Sum Equals K
# Medium
#
# 1767
#
# 44
#
# Favorite
#
# Share
# Given an array of integers and an integer k, you need to find the total number of
# continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter()
        counter[0] = 1
        total = 0
        total_count = 0
        for item in nums:
            total += item
            total_count += counter[total - k]
            counter[total] += 1
        return total_count

