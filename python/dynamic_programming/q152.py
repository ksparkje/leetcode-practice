# 152. Maximum Product Subarray
#
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


'''
Quite insightful question...
Notice, if we have odd number of negatives, between a subsequence (possibly split by 0s),
    that's when things get interesting.

EXAMPLE    [-2,         3,   4,  -5,   6,    -7]
from left  [-2,        -6, -24, 120, 720, -5040]-> direction
from right [-5040,   2520, 840, 210, -42,    -7] <- direction

If we have even number of negatives, then either direction doesn't really matter?

'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Either start from myself, or continue with prev * myself, or don't use it.
        # We can do this in reverse to get the       next * myself
        # Above comments would be true if it had less than 1, but since it's all integers
        # We only care about the whole product
        left_to_right = nums[:]
        right_to_left = nums[::-1]

        for idx in range(1, len(nums)):
            # if nums[idx-1] is 0, multiply 1
            left_to_right[idx] *= left_to_right[idx-1] or 1
            right_to_left[idx] *= right_to_left[idx-1] or 1
        return max(left_to_right + right_to_left)




