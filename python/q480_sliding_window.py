# 480. Sliding Window Median

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
# https://leetcode.com/problems/sliding-window-median/discuss/96355/Easy-Python-O(nk)

'''
Obviously, as long as the window is sorted, we can get the median easily.
As we walk down, remove the first elem and add the new elem
'''
import bisect

'''
God-like solution by 
# https://leetcode.com/problems/sliding-window-median/discuss/96355/Easy-Python-O(nk)
'''
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        medians = []

        # ... + [0] because item is added first to median, then computes window
        #       [0] can be anything...
        for to_remove, to_add in zip(nums, nums[k:] + [0]):
            medians.append((window[k//2] + window[~(k//2)]) / 2)
            window.remove(to_remove)
            bisect.insort(window, to_add)

        return medians

