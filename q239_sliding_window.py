# 239. Sliding Window Maximum
#
# Given an array nums, there is a sliding window of size k which is moving from the very left of
# the array to the very right. You can only see the k numbers in the window. Each time the sliding
# window moves right by one position. Return the max sliding window.
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
import bisect


'''
NOT AS EASY AS IT LOOKS
CRUX: current_window should be sorted descending
To keep the window descending, pop from the right when adding new element!
'''
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        current_window = sorted(nums[:k])
        answer = []

        for to_remove, to_add in zip(nums, nums[k:] + [0]):
            answer.append(current_window[-1])
            current_window.remove(to_remove)
            bisect.insort(current_window, to_add)

        return answer

    def maxSlidingWindow(self, nums, k: int):
        '''
        :param nums: All numbers in a sequence
        :param k: Sliding window of size k
        :return: list of integers, each elem of max of window of size k
        '''
        len_nums = len(nums)
        if len_nums == 0:
            return []
        if len_nums < k:
            return [max(nums)]

        # cur_window is sorted descending
        cur_window = []
        for idx, elem in enumerate(nums[:k]):
            while cur_window and cur_window[-1][0] < elem:
                cur_window.pop()
            cur_window += [(elem, idx)]

        so_far = [cur_window[0][0]]

        for idx, elem in enumerate(nums[k:], k):
            if cur_window and idx - cur_window[0][1] >= k:
                cur_window.pop(0)

            # corner case where the elem is the largest
            if cur_window and elem >= cur_window[0][0]:
                cur_window = [(elem, idx)]
            else:
                # while the right most elem of the current window is less than this elem
                while cur_window and cur_window[-1][0] < elem:
                    cur_window.pop()
                cur_window.append((elem, idx))

            so_far += [cur_window[0][0]]

        return so_far