# 153. Find Minimum in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated
# at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
# Input: [3,4,5,1,2]
# Output: 1
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
from typing import List


'''
Kinda just bothersome question, but interesting implementations possible
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        # There can be cases like sorted already
        if nums[0] < nums[-1]:
            return nums[0]

        first_elem = nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if first_elem > nums[mid]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([3,4,5,0,1,2]))
    print(s.findMin([4,5,0,1,2]))
    print(s.findMin([0,1,2]))
    print(s.findMin([0,1]))
    print(s.findMin([1,0]))





