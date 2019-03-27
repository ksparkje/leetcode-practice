# 53. Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which
# has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and
# conquer approach, which is more subtle.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Either I include myself only, or include all the subsequent sum + myself
        cur_sum = max_so_far = -float('inf')

        for item in nums:
            cur_sum = max(cur_sum + item, item)
            max_so_far = max(cur_sum, max_so_far)

        return max_so_far