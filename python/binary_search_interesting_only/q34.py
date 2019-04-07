# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the
# starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
'''
5, 7, 7, 8, 8, 10
F, F, F, T, T, T

5, 7, 7, 8, 8, 10
F, F, F, F, F, T

5, 7, 7, 8, 8, K = 9
F, F, F, F, F

2, 2, K = 2
F, F
'''
from operator import le, lt
from typing import List


'''
This is a typical question, but notice how it requires
left <= right to make my life easy...
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        def binary_search(operator):
            left, right = 0, len(nums) - 1
            while left <= right:
                # mid = (left + right) // 2
                mid = left + (right-left) // 2
                if operator(nums[mid], target):
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        first_left = binary_search(lt)
        second_left = binary_search(le) - 1     # Need to move one element left

        if first_left < len(nums) and \
                nums[first_left] == target and \
                first_left <= second_left:
            return [first_left, second_left]
        else:
            return [-1, -1]


if __name__ == '__main__':

    l = [2, 2]
    s = Solution()
    print(s.searchRange(l, 2))





















