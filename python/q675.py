# 675. Cut Off Trees for Golf Event
# Hard

# You are asked to cut off trees in a forest for a golf event.
# The forest is represented as a non-negative 2D map, in this map:
#
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.

# The place with number bigger than 1 represents a tree can be walked through,
# and this positive number represents the tree's height.
#
# You are asked to cut off all the trees in this forest in the order of tree's
# height - always cut off the tree with lowest height first. And after cutting,
# the original place has the tree will become a grass (value 1).
#
# You will start from the point (0, 0) and you should output the minimum steps
# you need to walk to cut off all the trees. If you can't cut off all the trees,
# output -1 in that situation.
#
# You are guaranteed that no two trees have the same height and there is at
# least one tree needs to be cut off.

# Example 1:
#
# Input:
# [
#  [1,2,3],
#  [0,0,4],
#  [7,6,5]
# ]
# Output: 6
#
# Example 2:
#
# Input:
# [
#  [1,3,4],
#  [0,2,0],
#  [7,6,5]
# ]
# Output: 10
#
# Example 3:
#
# Input:
# [
#  [2,3,4],
#  [0,0,5],
#  [8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.

from typing import List


'''
graph problem, start from (0,0). move right, left, up, down?

If seperate islands, impossible.
else:
    possible
    Function: Need to figure out the distance from the current node to the next.
    With sorted list ordered by the height, height != 1, try finding the distance
    from each of them. Then, add those distances until we have finished reaching to
    the last one.
    
TLE solution written by me, 36 / 53 test cases passed.
'''
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        len_i = len(forest)
        len_j = len(forest[0])

        def get_distance_from_s_to_t_bfs(si, sj, ti, tj):
            visited = set()
            queue = [(si, sj, 0)]

            while queue:
                cur_i, cur_j, cur_step = queue.pop(0)
                valid = 0 <= cur_i < len_i and 0 <= cur_j < len_j and forest[cur_i][cur_j] > 0

                if valid and (cur_i, cur_j) not in visited:
                    visited.add((cur_i, cur_j))
                    if (cur_i, cur_j) == (ti, tj):
                        return cur_step
                    else:
                        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            queue.append((cur_i + di, cur_j + dj, cur_step + 1))
            return -1

        trees_height_i_j = sorted((height, i, j)
                                  for i, row in enumerate(forest)
                                  for j, height in enumerate(row)
                                  if height > 1)

        si, sj, steps = 0, 0, 0
        for height, ti, tj in trees_height_i_j:
            this_step = get_distance_from_s_to_t_bfs(si, sj, ti, tj)
            if this_step == -1:
                return -1
            steps += this_step
            si, sj = ti, tj

        return steps


if __name__ == '__main__':
    s = Solution()
    forest = [[1,2,3],[0,0,4],[7,6,5]]
    print(s.cutOffTree(forest))

