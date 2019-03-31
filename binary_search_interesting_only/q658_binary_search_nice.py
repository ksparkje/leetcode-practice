# 658. Find K Closest Elements
# Medium
#
# Given a sorted array, two integers k and x, find the k closest elements to
# x in the array. The result should also be sorted in ascending order. If
# there is a tie, the smaller elements are always preferred.
#
# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 104
# Absolute value of elements in the array and x will not exceed 104

'''
Suppose a list:      0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   k = 4, x = 6      F, F, F, F, T, T, T, T, T, T,  T
   return = [4, 5, 6, 7]
   The question is, How do I find the first T condition?
   Think about (respect to x), how far away arr[left] is from arr[left + k].

   suppose idx = 4, x = 6, k = 4
   6 - arr[idx] = 6 - 4 <= arr[idx + 4] - 6
       ------            ----------
   left most elem        right most elem
'''


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left: left + k]







