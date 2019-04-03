# 540. Single Element in a Sorted Array
# Medium
#
# 672
#
# 57
#
# Favorite
#
# Share
# Given a sorted array consisting of only integers where every element appears twice except for
# one element which appears once. Find this single element that appears only once.
#
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.
from typing import List
from functools import reduce


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] != nums[mid ^ 1]:
                right = mid
            else:
                left = mid + 1

        return nums[left]

    def singleNonDuplicateReduce(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums, 0)


if __name__ == '__main__':
    input = [1,1,2,3,3,4,4,8,8]

    s = Solution()
    print(s.singleNonDuplicate(input))

