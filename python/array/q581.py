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
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103067/Python-O(N)-with-O(1)-space-complexity.-No-sorting
Suppose input: 
[1, 3, 7, 2, 5, 4, 6, 10]

left = 0, left += 1...
The moment I see a decreasing (A[left] > A[left + 1]), 
    that's the index I must at least swap.

right = len(A) - 1, right -= 1...
The moment I see increasing from the right (A[right-1] > A[right]), 
    that's the index I must at least swap.

               right
               |
1, 3, 7, 2, 5, 4, 6, 10
      |
      left   

Now (we are not done), the lowest and the highest from A[left:right+1]
    can at least tell us the lowest and the highest in the unsorted part 
    (unsorted part is unknown yet).
'''
class Solution:
    def findUnsortedSubarray(self, A: List[int]) -> int:
        if not A or len(A) < 2:
            return 0

        left, right = 0, len(A) - 1

        while left < len(A) - 1 and A[left] <= A[left + 1]:
            left += 1
        while right and A[right - 1] <= A[right]:
            right -= 1

        if right == 0:
            return 0

        min_val_unsorted = min(A[left: right+1])
        max_val_unsorted = max(A[left: right+1])

        while left and A[left-1] > min_val_unsorted:
            left -= 1
        while right < len(A) - 1 and A[right+1] < max_val_unsorted:
            right += 1

        return right - left + 1


class Solution3:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)


'''
This is strictly increasing or strictly decreasing!
'''
class Solution2:
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
