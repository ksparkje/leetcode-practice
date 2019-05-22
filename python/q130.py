# 130. Surrounded Regions
# Medium

# Given a 2D board containing 'X' and 'O' (the letter O), capture all
# regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any 'O' on the
# border of the board are not flipped to 'X'. Any 'O' that is not on the border and
# it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are
# connected if they are adjacent cells connected horizontally or vertically.
from typing import List


'''
Iterate through 0, 0 -> max_x, 0 -> max_x, max_y -> 0, max_y
    Try bfs and convert all O to 1
Iterate all points
    O if 1 else X
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return

        m, n = len(board), len(board[0])

        def predicate(i, j):
            return 0 <= i < m and 0 <= j < n and board[i][j] == 'O'

        to_iter = [(i, j)
                   for i in range(m)
                   for j in range(n)
                   if predicate(i, j) and (i in (0, m-1) or j in (0, n-1))]

        while to_iter:
            cur_i, cur_j = to_iter.pop()
            board[cur_i][cur_j] = 1

            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):

                temp_i, temp_j = cur_i + di, cur_j + dj

                if predicate(temp_i, temp_j):
                    to_iter.append((temp_i, temp_j))

        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 1 else 'X'


if __name__ == '__main__':
    s = Solution()

    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    s.solve(board)
    print(board)


























