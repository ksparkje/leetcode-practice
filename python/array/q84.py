# 84. Largest Rectangle in Histogram
# Hard
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the histogram.
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        increasing = []
        heights = [0] + heights + [0]
        max_area = 0

        for idx, h in enumerate(heights):
            while increasing and increasing[-1][1] >= h:
                # calculate the area
                pop_idx, pop_h = increasing.pop()
                left_idx = increasing[-1][0] if increasing else 0
                area = (idx - left_idx - 1) * pop_h
                max_area = max(area, max_area)
            increasing.append([idx, h])

        return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Notice, I should be concerned about the minimum number...
        # I need to know when this low number ends.
        # Therefore, I need a increasing sequence.
        if not heights:
            return 0

        increasing = []
        cur_best = 0
        # heights = [0] + heights + [0]
        heights = heights + [0]

        for idx, height in enumerate(heights):
            while increasing and height <= increasing[-1][1]:
                pop_idx, pop_height = increasing.pop()

                width = idx if not increasing else idx - 1 - increasing[-1][0]
                area = width * pop_height
                cur_best = max(cur_best, area)

            # while increasing and height < increasing[-1][1]:
            #     pop_idx, pop_height = increasing.pop()
            #
            #     left_distance = pop_idx - increasing[-1][0] - 1 if increasing else 0
            #     right_distance = idx - pop_idx
            #     area = (right_distance + left_distance) * pop_height
            #
            #     cur_best = max(cur_best, area)

            increasing.append([idx, height])

        return cur_best


if __name__ == '__main__':
    s = Solution()

    heights = [0, 9]
    heights = [2, 1, 0, 5, 6, 2, 3]
    heights = [2, 1, 2]

    print(s.largestRectangleArea(heights))