# 632. Smallest Range
# Hard
#
# 634
#
# 19
#
# You have k lists of sorted integers in ascending order.
# Find the smallest range that includes at least one number from each of the k lists.
#
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
#
# Example 1:
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Note:
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -105 <= value of elements <= 105.
import bisect
from typing import List


'''
Funny thing is, when the minimum item is coming from a list, and it's the last elem,
    there is no way we could improve the answer, so we break!

i.e. 
[2, 10, 22]
[3, 9]
[6, 14, 19, 24]

If the second is ended with 9, and 9 is the lowest number, we can't improve the range!
'''
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        max_indecies = [len(item)-1 for item in nums]
        queue = list(sorted([nums[idx][0], idx, 0] for idx in range(len(nums))))
        min_range_so_far = [queue[0][0], queue[-1][0]]

        while True:
            cur_item, idx_in_k, cur_idx = queue.pop(0)
            # final item
            if cur_idx == max_indecies[idx_in_k]:
                break
            new_item = [nums[idx_in_k][cur_idx + 1], idx_in_k, cur_idx + 1]
            bisect.insort_left(queue, new_item)
            if min_range_so_far[1] - min_range_so_far[0] > queue[-1][0] - queue[0][0]:
                min_range_so_far = [queue[0][0], queue[-1][0]]

        return min_range_so_far


if __name__ == '__main__':
    given = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

    s = Solution()
    print(s.smallestRange(given))



















