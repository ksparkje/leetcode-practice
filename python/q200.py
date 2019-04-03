# 200. Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.
from typing import List


'''
It's possible DFS > BFS!!!
'''
class Solution:
    def delta_y_delta_x(self, i, j):
        so_far = []
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            so_far.append((i+dy, j+dx))
        return so_far

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        so_far = set()
        count = 0

        len_i = len(grid)
        len_j = len(grid[0])

        for i in range(len_i):
            for j in range(len_j):
                if grid[i][j] == '1' and ((i, j) not in so_far):
                    count += 1
                    queue = [(i, j)]

                    while queue:
                        cur_node = queue.pop(0)

                        if cur_node not in so_far:
                            # mark it as visitied
                            so_far.add(cur_node)

                            positions = self.delta_y_delta_x(*cur_node)
                            for cur_i, cur_j in positions:
                                if (0 <= cur_i < len_i and
                                    0 <= cur_j < len_j and
                                    (cur_i, cur_j) not in so_far and
                                    grid[cur_i][cur_j] == '1'):

                                    queue.append((cur_i, cur_j))

        return count

    def dfs_solution(self, grid):
        len_i = len(grid)
        len_j = len(grid[0])

        def sink(i, j):
            if 0 <= i < len_i and 0 <= j < len_j and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            else:
                return 0

        return sum(sink(i, j) for i in range(len_i) for j in range(len_j))


if __name__ == '__main__':
    s = Solution()

    input = [["1","1","1"],["0","1","0"],["1","1","1"]]
    print(s.numIslands(input))