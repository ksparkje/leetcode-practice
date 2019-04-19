# 18. 4Sum
# Medium
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
import bisect
from collections import Counter
from typing import List

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        def twoSum(nums, target):

            counter = Counter(nums)

            so_far = []
            for idx, item in enumerate(nums):
                if idx and nums[idx-1] == item:
                    continue

                diff = target - item
                if item > diff:
                    continue

                if diff == item:
                    if counter[item] > 1:
                        so_far.append([item, item])

                else:
                    if diff in counter:
                        so_far.append([item, diff])

            return so_far
            # if len(nums) == 0:
            #     return []
            # l = 0
            # r = len(nums) - 1
            # result = []
            # while l < r:
            #     s = nums[l] + nums[r]
            #     if s == target:
            #         result.append([nums[l], nums[r]])
            #         while l + 1 < r and nums[l + 1] == nums[l]:
            #             l += 1
            #         while l < r - 1 and nums[r - 1] == nums[r]:
            #             r -= 1
            #         l, r = l + 1, r - 1
            #     elif s < target:
            #         l += 1
            #     else:
            #         r -= 1
            # return result

        def nSum(nums, target, n):
            res = []
            if n == 2:
                return twoSum(nums, target)
            else:
                for idx, num in enumerate(nums):
                    if idx and num == nums[idx - 1]:
                        continue
                    next_res = nSum(nums[idx + 1:], target - num, n - 1)
                    for ns in next_res:
                        if len(ns) == n - 1:
                            res.append([num] + ns)
            return res

        return nSum(nums, target, 4)


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]

    s = Solution()
    print(s.fourSum(nums, 0))


