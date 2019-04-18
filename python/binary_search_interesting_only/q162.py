# 162. Find Peak Element
# Medium
#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and
# return its index.
#
# The array may contain multiple peaks, in that case return the index to any one
# of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
#              or index number 5 where the peak element is 6.
# Note:
#
# Your solution should be in logarithmic complexity.

'''
Somewhat interesting...
1, 2, 3, 4, 3, 2, 1, ...

Suppose I test the idea such that
1, 2, 3, 4, 3, 2, 1, ...
T, T, T, T, F, F, F

Equivalently,
if A[mid-1] <= A[mid]:
    left = mid
else:
    right = mid - 1

But notice this is troublesome, b/c (0 + 1) // 2 = 0. Fix by
    mid = left + (right - left + 1) // 2 ? This pushes mid
    to one index right.
'''
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left + 1) // 2

            if nums[mid-1] <= nums[mid]:
                left = mid
            else:
                right = mid - 1

        # Return the index
        # return nums[left]
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([1,2,3,4,3,2,1]))
    print(s.findPeakElement([1,2,3,4]))
    print(s.findPeakElement([4,3,2,1]))
    print(s.findPeakElement([]))
    print(s.findPeakElement([1,2]))
    print(s.findPeakElement([2]))
    print(s.findPeakElement([1,2,3,0,2,3,4]))
    print(s.findPeakElement([1,2,3,2,3,4]))
    print(s.findPeakElement([1,3,2,3,4]))





































