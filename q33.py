# 33. Search in Rotated Sorted Array
# Medium
#
# 2122
#
# 294
#
# Favorite
#
# Share
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


'''
case 1. target > first elem
    Find the max value first?
    Then do the search in between

case 2. target < first elem
    Find the min value first?
    Then do the search in between
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        first_num = nums[0]

        def find_max_index():
            # Notice, things go wrong if len == 1
            left_, right_ = 0, len(nums) - 1
            while left_ < right_:
                mid = (left_+right_)//2
                # This has to be >=
                if nums[mid] >= first_num:
                    left_ = mid + 1
                else:
                    right_ = mid
            return left_ - 1

        # When everything sorted, nothing on the back...
        # Must be <= to ensure one element case
        if nums[0] <= nums[-1]:
            max_index = len(nums) - 1
        else:
            max_index = find_max_index()

        if first_num <= target:
            left, right = 0, max_index
        else:
            left = 0 if max_index == len(nums) - 1 else max_index + 1
            right = len(nums) - 1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == '__main__':
    s = Solution()
    # print(s.search([5,6,7,0,2,3], 6))
    # print(s.search([3,4,1,2], 1))
    print(s.search([4,1,2], 4))
    print(s.search([3,1], 3))








































