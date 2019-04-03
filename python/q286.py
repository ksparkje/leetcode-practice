# 286. Walls and Gates

# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
# represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to
# reach a gate, it should be filled with INF.
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return

        # Find the gates
        queue = [(i, j, 0)
                 for i, row in enumerate(rooms)
                 for j, val in enumerate(row) if val == 0]

        while queue:
            # get the current position
            i, j, dist = queue.pop(0)
            # Record my current distance if i am an empty room
            if not dist or dist < rooms[i][j]:
                rooms[i][j] = dist

                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni, nj = i + di, j + dj
                    if (0 <= ni < len(rooms) and
                        0 <= nj < len(rooms[0]) and
                        dist + 1 < rooms[ni][nj]):
                        queue.append((ni, nj, dist + 1))


if __name__ == '__main__':

    rooms = [[2147483647,-1,0,2147483647],
             [2147483647,2147483647,2147483647,-1],
             [2147483647,-1,2147483647,-1],
             [0,-1,2147483647,2147483647]]

    s = Solution()
    s.wallsAndGates(rooms)

