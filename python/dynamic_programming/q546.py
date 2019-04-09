# 546. Remove Boxes
# Hard
#
# Given several boxes with different colors represented by different positive numbers.
# You may experience several rounds to remove boxes until there is no box left. Each
# time you can choose some continuous boxes with the same color (composed of k boxes,
# k >= 1), remove them and get k*k points.

# Find the maximum points you can get.
#
# Example 1:
# Input:
#
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# Output:
# 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
# ----> [1, 3, 3, 3, 1] (1*1=1 points)
# ----> [1, 1] (3*3=9 points)
# ----> [] (2*2=4 points)
# Note: The number of boxes n would not exceed 100.


'''
Try deleting boxes starting from left to right.
Delete boxes not the same as the contiguous.
'''
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def get_start_end(given_list, starting_idx):
            starting_item = given_list[starting_idx]
            for idx, item in enumerate(given_list[starting_idx:],
                                       starting_idx):
                if item != starting_item:
                    return starting_idx, idx
            return starting_idx, idx+1

        def dfs(boxes_remaining):
            if not boxes_remaining:
                return 0
            if len(boxes_remaining) == 1:
                return 1

            t_boxes = tuple(boxes_remaining)
            if t_boxes in visited:
                return visited[t_boxes]

            max_points_so_far = 0
            possible_start_endings = []
            ending_idx = 0

            for idx, item in enumerate(boxes_remaining):
                if idx == 0 or idx >= ending_idx:
                    start_end = get_start_end(boxes_remaining, idx)
                    if start_end:
                        possible_start_endings.append(start_end)
                    ending_idx = start_end[-1]

            for start_idx, end_idx in possible_start_endings:
                this_point = (end_idx - start_idx) ** 2 + dfs(boxes_remaining[:start_idx] +
                                                              boxes_remaining[end_idx:])
                max_points_so_far = max(this_point, max_points_so_far)

            visited[t_boxes] = max_points_so_far
            return max_points_so_far

        visited = {}
        return dfs(boxes)


if __name__ == '__main__':
    s = Solution()
    input = [1, 3, 2, 2, 2, 3, 4, 3, 1]
    print(s.removeBoxes(input))







