# 581. Shortest Unsorted Continuous Subarray
# Given an integer array, you need to find one continuous subarray that if
# you only sort this subarray in ascending order, then the whole array will
# be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.
from typing import List


'''
This is strictly increasing or strictly decreasing!
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        increasing = []
        length = len(nums)
        left_bound = length
        for idx, item in enumerate(nums):
            while increasing and increasing[-1][1] > item:
                left_bound = min(left_bound, increasing.pop()[0])
            increasing.append([idx, item])

        decreasing = []
        right_bound = 0
        for idx, item in reversed(list(enumerate(nums))):
            while decreasing and decreasing[-1][1] < item:
                right_bound = max(right_bound, decreasing.pop()[0])
            decreasing.append([idx, item])

        return right_bound - left_bound + 1 if right_bound else 0


if __name__ == '__main__':
    s = Solution()

    input = [1,2,3,3,3]
    print(s.findUnsortedSubarray(input))
