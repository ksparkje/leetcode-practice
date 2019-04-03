# 289. Game of Life
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John Horton
# Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
# using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current
#   state. The next state is created by applying the above rules simultaneously to every cell in
#   the current state, where births and deaths occur simultaneously.


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_3x3(i, j):
            starting_y = max(i - 1, 0)
            ending_y = min(i + 1, max_y - 1)

            starting_x = max(j - 1, 0)
            ending_x = min(j + 1, max_x - 1)

            return starting_y, starting_x, ending_y, ending_x

        def count_ones(starting_y, starting_x, ending_y, ending_x):
            counter = 0
            for _y in range(starting_y, ending_y + 1):
                for _x in range(starting_x, ending_x + 1):
                    counter += board[_y][_x]
            return counter

        max_y = len(board)
        max_x = len(board[0])

        live_die_board = [[0] * max_x for _ in range(max_y)]

        for y in range(max_y):
            for x in range(max_x):
                count = count_ones(*get_3x3(y, x))
                if board[y][x]: # my cell is alive
                    count -= 1
                    if 2 <= count <= 3:
                        live_die_board[y][x] = 1

                else:
                    if count == 3:
                        live_die_board[y][x] = 1

        for y in range(max_y):
            for x in range(max_x):
                board[y][x] = live_die_board[y][x]








