# 694. Number of Distinct Islands
# Medium
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same
# as another if and only if one island can be translated (and not rotated or
# reflected) to equal the other.

# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.

# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.


'''
Build graph when we visit nodes
such that each graph is indexed from [0,0] -> [0 + len_y, 0 + len_x]

Then keep it into a dictionary
'''

from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        so_far = set()

        # Do dfs on [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i ,j):
            '''
            :param i:
            :param j:
            :return: points in a list
            '''
            _so_far = []
            if grid[i][j]:
                # Mark it `0` when visiting
                grid[i][j] = 0
                _so_far.append([i, j])

                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    # if it's in the grid
                    if 0 <= i + di < len_i and 0 <= j + dj < len_j:
                        _so_far += dfs(i + di, j + dj)

            return _so_far

        len_i = len(grid)
        len_j = len(grid[0])

        for i in range(len_i):
            for j in range(len_j):
                # Visit from each of the point
                if grid[i][j]:
                    # Put it into current_graph
                    cur_graph = dfs(i, j)

                    to_so_far = []
                    # Make sure I place each point as relative to (0,0), and make it a set
                    for i1, j1 in cur_graph:
                        to_so_far += [(i1 - i, j1 - j)]

                    # Once done, put current_graph into so_far
                    so_far.add(tuple(to_so_far))

        return len(so_far)


if __name__ == '__main__':
    s = Solution()

    print(s.numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))



