# 221. Maximal Square
# Medium
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing
# only 1's and return its area.
#
# Example:
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # I think it's better to turn this matrix into List[List[int]]
        matrix = [[int(i) for i in row] for row in matrix]

        if not matrix:
            return 0

        len_i = len(matrix)
        len_j = len(matrix[0])
        so_far = {}

        # Helper function that tells me how many moves I can make
        def f(i, j) -> int:
            if (i, j) in so_far:
                return so_far[i, j]

            min_move = 0

            if matrix[i][j]:
                right_i, right_j = i, j+1
                diag_i, diag_j = i+1, j+1
                down_i, down_j = i+1, j

                if all(0 <= i_idx < len_i for i_idx in [right_i, diag_i, down_i]) and \
                    all(0 <= j_idx < len_j for j_idx in [right_j, diag_j, down_j]):

                    if all(item for item in [matrix[right_i][right_j],
                                             matrix[diag_i][diag_j],
                                             matrix[down_i][down_j]]):

                        right = f(i, j+1)
                        diag = f(i+1, j+1)
                        down = f(i+1, j)

                        min_move = min(right, diag, down) + 1

            so_far[i, j] = min_move
            return min_move

        best_so_far = 0
        for i in range(len_i):
            for j in range(len_j):
                if matrix[i][j]:
                    moves_possible = f(i, j)
                    square_size = (1 + moves_possible) ** 2
                    best_so_far = max(best_so_far, square_size)

        return best_so_far


'''
Better solution from Discussion
https://leetcode.com/problems/maximal-square/discuss/164120/Python-or-DP-tm
'''
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0

        res = max(max(row) for row in dp)
        return res ** 2


if __name__ == '__main__':
    s = Solution()
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]

    print(s.maximalSquare(matrix))


