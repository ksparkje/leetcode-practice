# https://leetcode.com/problems/contiguous-array

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
#   Input: [0,1]
#   Output: 2
#   Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
#   Input: [0,1,0]
#   Output: 2
#   Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

class Solution(object):
    def findMaxLength(self, given_array):
        """
        :type nums: List[int]
        :rtype: int
        """

        so_far = [0] * (len(given_array) + 1)
        for i, item in enumerate(given_array, 1):
            prev_item = so_far[i-1]
            so_far[i] = prev_item + 1 if item == 1 else prev_item - 1

        global_max = 0
        min_max_dict = {}
        for i, item in enumerate(so_far):
            if item in min_max_dict:
                global_max = max(global_max, i - min_max_dict[item])
            else:
                # item is not in min_max, so give min for the item
                min_max_dict[item] = i

        return global_max

