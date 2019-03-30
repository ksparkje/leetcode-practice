# 378. Kth Smallest Element in a Sorted Matrix
# Medium
#
# Given a n x n matrix where each of the rows and columns are sorted in ascending order,
# find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        min_heap = [(matrix[0][0], 0, 0)]
        so_far = []
        visited = set()

        while min_heap and len(so_far) < k:
            value, i, j = heapq.heappop(min_heap)
            so_far.append(value)
            for di, dj in ((0, 1), (1, 0)):
                new_i = i + di
                new_j = j + dj
                if (0 <= new_i < len(matrix) and
                    0 <= new_j < len(matrix[0]) and
                    (new_i, new_j) not in visited):
                    visited.add((new_i, new_j))
                    heapq.heappush(min_heap, (matrix[new_i][new_j], new_i, new_j))

        return so_far[k-1]

