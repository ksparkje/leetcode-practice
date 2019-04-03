# 85. Maximal Rectangle
# Hard
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing
# only 1's and return its area.
#
# Example:
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6
from typing import List


# The idea used to solve q84 under array is what's used to solve.
# Possibly, q221 could be a help, but not sure how exactly I'd do it.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Notice, I should be concerned about the minimum number...
        # I need to know when this low number ends.
        # Therefore, I need a increasing sequence.
        if not heights:
            return 0

        increasing = []
        cur_best = 0
        heights = [0] + heights + [0]
        for idx, height in enumerate(heights):
            while increasing and height < increasing[-1][1]:
                pop_idx, pop_height = increasing.pop()

                left_distance = pop_idx - increasing[-1][0] - 1 if increasing else 0
                right_distance = idx - pop_idx
                area = (right_distance + left_distance) * pop_height

                cur_best = max(cur_best, area)

            increasing.append([idx, height])

        return cur_best

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        matrix = [list(map(lambda x: int(x), row)) for row in matrix]
        len_i, len_j = len(matrix), len(matrix[0])
        max_so_far = self.largestRectangleArea(matrix[0])

        for i in range(1, len_i):
            for j in range(len_j):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]

            max_here = self.largestRectangleArea(matrix[i])
            max_so_far = max(max_so_far, max_here)

        return max_so_far







