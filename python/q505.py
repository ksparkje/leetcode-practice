# 505. The Maze II
# There is a ball in a maze with empty spaces and walls. The ball can go through empty
# spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall.
# When the ball stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze, find the shortest distance
# for the ball to stop at the destination. The distance is defined by the number of empty spaces
# traveled by the ball from the start position (excluded) to the destination (included). If the
# ball cannot stop at the destination, return -1.
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space.
# You may assume that the borders of the maze are all walls. The start and destination coordinates
# are represented by row and column indexes.
#

# Example 1:
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 S
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 D
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
#
# Output: 12
# There is picture in the original posting...
from typing import List


'''
Try BFS first

Check if current position is the Destination
Then, add my neighbors from current positions
'''
class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n, q, stopped = (len(maze),
                            len(maze[0]),
                            [(0, start[0], start[1])],
                            {(start[0], start[1]):0})
        while q:
            dist, x, y = heapq.heappop(q)
            if [x, y] == destination:
                return dist
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1

                if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = dist + d
                    heapq.heappush(q, (dist + d, newX, newY))
        return -1


    def shortestDistanceBFS(self,
                            maze: List[List[int]],
                            start: List[int],
                            destination: List[int]) -> int:

        len_y = len(maze)
        len_x = len(maze[0])

        def get_next(given_position):

            ans = []
            for di, dj in [(1,0), (-1, 0), (0,-1), (0,1)]:
                y, x = given_position
                count = 0
                while 0 <= y + di < len_y and 0 <= x + dj < len_x and (maze[y+di][x+dj] == 0):
                    y, x = y + di, x + dj
                    count += 1
                if (y, x) not in visited:
                    ans.append([[y, x], count])
            return ans

        tuple_start = [start, 0]
        queue = [tuple_start]
        visited = set([tuple(start)])
        found = False
        min_dist = len_y * len_x
        while queue:
            cur_position, dist = queue.pop(0)

            if cur_position == destination:
                min_dist = min(min_dist, dist)
                found = True

            for next_position, next_dist in get_next(cur_position):
                n = tuple(next_position)
                if n not in visited:
                    visited.add(n)
                    queue.append([next_position, dist + next_dist])

        return min_dist if found else -1



















































