# 238. Product of Array Except Self
#
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


'''
if accumulate multiplication?
1,  2,  3,  4
First pass, skip the current number and accumulate till the behind
1,  1,  2,  6
Second pass, do the reverse
24, 12, 8, 6


Behind by one is the idea!!!
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        so_far = [1] * len_nums
        left, right = 1, 1

        # One pass solution
        for idx in range(len_nums):
            so_far[idx] *= left
            so_far[~idx] *= right
            left *= nums[idx]
            right *= nums[~idx]

        # Two pass solution...
        # acc = 1
        # for idx, item in enumerate(nums):
        #     so_far[idx] = acc
        #     acc *= item

        # acc = 1
        # for idx, item in enumerate(reversed(nums)):
        #     so_far[~idx] *= acc
        #     acc *= item

        return so_far
