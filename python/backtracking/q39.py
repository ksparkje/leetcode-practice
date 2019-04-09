# 39. Combination Sum
# Medium
#
# Given a set of candidate numbers (candidates) (without duplicates) and a target
# number (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]

# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start_idx, path, remaining):
            if remaining == 0:
                so_far.append(path)
                return
            if remaining < 0:
                return

            for idx, item in enumerate(candidates[start_idx:], start_idx):
                dfs(idx, path + [item], remaining - item)

        if not candidates:
            return []

        candidates.sort()
        so_far = []
        dfs(0, [], target)
        return so_far


if __name__ == '__main__':
    candidates = [2,3,5]
    target = 8
    s = Solution()
    print(s.combinationSum(candidates, target))
