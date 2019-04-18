# 300. Longest Increasing Subsequence
# Medium
#
# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to return the
# length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?


'''
DP :
    Suppose I pick an index i (ending at index i).

    for j in range(i): # j is a starting point
        if A[j] < A[i]:
            max_count[i] = max(max_count[j]+1, max_count[i])

Slow...
'''
class Solution(object):
    def lengthOfLISSlow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        max_count = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    max_count[i] = max(max_count[i], max_count[j]+1)

        return max(max_count)


'''
https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

Suppose [4, 6, 8, 0, 3, 4, 5]

[4]
--- add 6
[4]
[6] -> equivalent to [4, 6]
--- add 8
[4]
[6] -> equivalent to [4, 6]
[8] -> equivalent to [4, 6, 8]
--- add 0
[0]
[6] -> equivalent to [4, 6]     Notice, don't worry about 0 for now
[8] -> equivalent to [4, 6, 8]  Notice, don't worry about 0 for now
--- add 3
[0]
[3] -> equivalent to [0, 3]
[8] -> equivalent to [4, 6, 8]
--- add 4
[0]
[3] -> equivalent to [0, 3]
[4] -> equivalent to [0, 3, 4]
--- add 5
[0]         length 1
[3]         length 2
[4]         length 3
[5]         length 4
'''
import bisect


class Solution2:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        so_far = []
        for item in nums:
            if not so_far:
                so_far += [item]
            else:
                if item < so_far[0]:
                    so_far[0] = item
                elif item > so_far[-1]:
                    so_far.append(item)
                else:
                    idx_to_insert = bisect.bisect_left(so_far, item)
                    so_far[idx_to_insert] = item
        return len(so_far)


# In general, we have set of active lists of varying length.
# We are adding an element A[i] to these lists. We scan the lists
# (for end elements) in decreasing order of their length. We will
# verify the end elements of all the lists to find a list whose end
# element is smaller than A[i] (floor value).

# Our strategy determined by the following conditions,
#
# 1. If A[i] is smallest among all end
#    candidates of active lists, we will start
#    new active list of length 1.

# 2. If A[i] is largest among all end candidates of
#   active lists, we will clone the largest active
#   list, and extend it by A[i].
#
# 3. If A[i] is in between, we will find a list with
#   largest end element that is smaller than A[i].
#   Clone and extend this list by A[i]. We will discard all
#   other lists of same length as that of this modified list.

# Note that at any instance during our construction of active lists, the
# following condition is maintained.
#
# “end element of smaller list is smaller than end elements of larger lists”.
#
# It will be clear with an example, let us take example from wiki
# {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15}.
#
# A[0] = 0. Case 1. There are no active lists, create one.
# 0.
# -----------------------------------------------------------------------------
# A[1] = 8. Case 2. Clone and extend.
# 0.
# 0, 8.
# -----------------------------------------------------------------------------
# A[2] = 4. Case 3. Clone, extend and discard.
# 0.
# 0, 4.
# 0, 8. Discarded
# -----------------------------------------------------------------------------
# A[3] = 12. Case 2. Clone and extend.
# 0.
# 0, 4.
# 0, 4, 12.
# -----------------------------------------------------------------------------
# A[4] = 2. Case 3. Clone, extend and discard.
# 0.
# 0, 2.
# 0, 4. Discarded.
# 0, 4, 12.
# -----------------------------------------------------------------------------
# A[5] = 10. Case 3. Clone, extend and discard.
# 0.
# 0, 2.
# 0, 2, 10.
# 0, 4, 12. Discarded.
# -----------------------------------------------------------------------------
# A[6] = 6. Case 3. Clone, extend and discard.
# 0.
# 0, 2.
# 0, 2, 6.
# 0, 2, 10. Discarded.
# -----------------------------------------------------------------------------
# A[7] = 14. Case 2. Clone and extend.
# 0.
# 0, 2.
# 0, 2, 6.
# 0, 2, 6, 14.
# -----------------------------------------------------------------------------
# A[8] = 1. Case 3. Clone, extend and discard.
# 0.
# 0, 1.
# 0, 2. Discarded.
# 0, 2, 6.
# 0, 2, 6, 14.
# -----------------------------------------------------------------------------
# A[9] = 9. Case 3. Clone, extend and discard.
# 0.
# 0, 1.
# 0, 2, 6.
# 0, 2, 6, 9.
# 0, 2, 6, 14. Discarded.
# -----------------------------------------------------------------------------
# A[10] = 5. Case 3. Clone, extend and discard.
# 0.
# 0, 1.
# 0, 1, 5.
# 0, 2, 6. Discarded.
# 0, 2, 6, 9.
# -----------------------------------------------------------------------------
# A[11] = 13. Case 2. Clone and extend.
# 0.
# 0, 1.
# 0, 1, 5.
# 0, 2, 6, 9.
# 0, 2, 6, 9, 13.
# -----------------------------------------------------------------------------
# A[12] = 3. Case 3. Clone, extend and discard.
# 0.
# 0, 1.
# 0, 1, 3.
# 0, 1, 5. Discarded.
# 0, 2, 6, 9.
# 0, 2, 6, 9, 13.
# -----------------------------------------------------------------------------
# A[13] = 11. Case 3. Clone, extend and discard.
# 0.
# 0, 1.
# 0, 1, 3.
# 0, 2, 6, 9.
# 0, 2, 6, 9, 11.
# 0, 2, 6, 9, 13. Discarded.
# -----------------------------------------------------------------------------
# A[14] = 7. Case 3. Clone, extend and discard.
# 0.
# 0, 1.
# 0, 1, 3.
# 0, 1, 3, 7.
# 0, 2, 6, 9. Discarded.
# 0, 2, 6, 9, 11.
# ----------------------------------------------------------------------------
# A[15] = 15. Case 2. Clone and extend.
# 0.
# 0, 1.
# 0, 1, 3.
# 0, 1, 3, 7.
# 0, 2, 6, 9, 11.
# 0, 2, 6, 9, 11, 15. <-- LIS List
# ----------------------------------------------------------------------------

