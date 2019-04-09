# 310. Minimum Height Trees
# Nice problem!

# Medium
#
# For an undirected graph with tree characteristics, we can choose any
# node as the root. The result graph is then a rooted tree. Among all
# possible rooted trees, those with minimum height are called minimum
# height trees (MHTs). Given such a graph, write a function to find all
# the MHTs and return a list of their root labels.
#
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will
# be given the number n and a list of undirected edges (each edge is a pair of labels).
#
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
#
# Example 1 :
#
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
#         0
#         |
#         1
#        / \
#       2   3
#
# Output: [1]

# Example 2 :
#
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
#
# Output: [3, 4]
# Note:
#
# According to the definition of tree on Wikipedia: “a tree is an undirected
# graph in which any two vertices are connected by exactly one path. In other
# words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.


'''
Idea is quite simple...
#      0  1  2
#       \ | / -------- CUT HERE
#         3
#         |
#         4
#         |   -------- CUT HERE
#         5
Answer is [3, 4]. Start with the nodes with no children. Get rid of those
children. Then go to the nodes with no children. Obviously, when getting
rid of the children, we have to keep track of which nodes no longer have
any children.
https://leetcode.com/problems/minimum-height-trees/discuss/76149/Share-my-Accepted-BFS-Python-Code-with-O(n)-Time
'''
from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for v1, v2 in edges:
            degree[v1] += 1
            degree[v2] += 1
            graph[v1].append(v2)
            graph[v2].append(v1)

        # get all the children
        previous_level = []
        for key, val in degree.items():
            if val == 1:
                previous_level.append(key)

        not_visited = set(range(n))

        # Number of root <= 2
        while len(not_visited) > 2:
            waiting = []
            for node in previous_level:
                not_visited.remove(node)

                for next_node in graph[node]:
                    if next_node in not_visited:
                        degree[next_node] -= 1
                        if degree[next_node] == 1:
                            waiting.append(next_node)
            previous_level = waiting

        return previous_level


if __name__ == '__main__':

    s = Solution()
    n, given = 4, [[1,0],[1,2],[1,3]]
    s.findMinHeightTrees(n, given)




