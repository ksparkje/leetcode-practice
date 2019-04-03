# 503. Next Greater Element II
# Medium
#
# Given a circular array (the next element of the last element is the first element of the array),
# print the Next Greater Number for every element. The Next Greater Number of a number x is the first
# greater number to its traversing-order next in the array, which means you could search circularly to
# find its next greater number. If it doesn't exist, output -1 for this number.
#
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.

'''
[1, 2, 4, 0, 8, 7]

[2]
[4]
[4, 0]
[8]
[8, 7]
[8, 7, 1]
[8, 7, 2]
[8, 7, 4]
[8, 7, 4, 0]

answer should be
[2,4,8,8,-1,8]

'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # We have to go at least one cycle
        # So might as well keep a counter to tell whether we've seen one
        cur_idx = aux_idx = 0
        stack = []
        ans = [-1] * len(nums)

        while aux_idx < (len(nums) * 2):
            cur_item = nums[cur_idx]

            while stack and stack[-1][-1] < cur_item:
                pop_idx, pop_item = stack.pop()
                ans[pop_idx] = cur_item

            stack.append([cur_idx, cur_item])

            aux_idx += 1
            cur_idx += 1
            cur_idx %= len(nums)

        return ans





