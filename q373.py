# 373. Find K Pairs with Smallest Sums
# Medium
#
# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
#
# Example 1:
#
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence:
#              [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:
#
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence:
#              [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:
#
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


'''
If you try to do it with O(k)... well I don't know. Not sure if it's feasible in 30 minutes.

Let's say O(k^2). Build a table such that row is one matrix, col the other.

Example (2)
    1,  1,  1
    ---------
1 | 2   2   2
2 | 3   3   4
3 | 4   4   5

Rings a bell? But you might be thinking a situation of given a target. Here, the question is,
k'th, not find a target. Might as well take an easy route and do bfs.

BFS: start with 0,0, obviously, and search for (right, down). push them into min-heap?

'''
from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 and not nums2 or len(nums1) == 0 or len(nums2) == 0:
            return []

        table = [[0]*len(nums2) for _ in range(len(nums1))]

        for i, n1 in enumerate(nums1):
            for j, n2 in enumerate(nums2):
                table[i][j] = n1 + n2

        min_heap = [(table[0][0], 0, 0)]
        so_far = []
        visited = set()

        while min_heap and len(so_far) < k:
            value, i, j = heapq.heappop(min_heap)
            so_far.append([nums1[i], nums2[j]])
            for di, dj in ((0, 1), (1, 0)):
                new_i = i + di
                new_j = j + dj
                if (0 <= new_i < len(nums1) and
                    0 <= new_j < len(nums2) and
                    (new_i, new_j) not in visited):
                    visited.add((new_i, new_j))
                    heapq.heappush(min_heap, (table[new_i][new_j], new_i, new_j))

        return so_far


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs([1,1,2], [1,2,3], 3))







































































