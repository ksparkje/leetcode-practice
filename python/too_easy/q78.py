# 78. Subsets
# Medium
#
# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start_idx, temp):
            so_far.append(temp)

            for idx in range(start_idx, length):
                backtrack(idx+1, temp + [nums[idx]])

        so_far = []
        length = len(nums)
        backtrack(0, [])
        return so_far




















