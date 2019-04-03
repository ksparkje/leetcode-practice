# 416. Partition Equal Subset Sum
# Medium
#
# 1085
#
# 30
#
# Given a non-empty array containing only positive integers, find if the array can be partitioned
# into two subsets such that the sum of elements in both subsets is equal.
#
# Note:
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
#
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        so_far = {}

        def dfs(remaining, starting_index):
            # return True if possible else False
            if remaining == 0:
                return True
            if remaining < 0:
                return False
            if remaining in so_far:
                return so_far[remaining]
            if starting_index > len(nums):
                return False

            cur_result = any(dfs(remaining - item, starting_index + i)
                             for i, item in enumerate(nums[starting_index:], 1))

            so_far[remaining] = cur_result
            return cur_result

        total = sum(nums)
        if total % 2:
            return False
        return dfs(total//2, 0)


if __name__ == '__main__':
    s = Solution()
    items = [1,2,3,5]
    print(s.canPartition(items))




