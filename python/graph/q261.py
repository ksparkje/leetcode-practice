# 261. Graph Valid Tree
# Medium
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges
# (each edge is a pair of nodes), write a function to check whether these
# edges make up a valid tree.
#
# Example 1:
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# Example 2:
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false

# Note: you can assume that no duplicate edges will appear in edges.
# Since all edges are undirected, [0,1] is the same as [1,0] and thus will
# not appear together in edges.
from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = [None] * n
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()

        def dfs(idx, parent=None):
            if nodes[idx] == 1:
                return True
            if nodes[idx] == -1:
                return False

            visited.add(idx)

            nodes[idx] = -1

            for node in graph[idx]:
                if node != parent and not dfs(node, idx):
                    return False

            nodes[idx] = 1

            return True

        return dfs(0) and len(visited) == n


if __name__ == '__main__':

    s = Solution()
    n = 4
    graph = [[0, 1], [0, 2], [0, 3], [1, 4]]
    graph = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    graph = [[0,1],[2,3]]
    print(s.validTree(n, graph))



