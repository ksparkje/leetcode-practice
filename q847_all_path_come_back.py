# 847. Shortest Path Visiting All Nodes
# Hard
#
# An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.
#
# graph.length = N, and j != i is in the list graph[i] exactly once, if and only if
# nodes i and j are connected.
#
# Return the length of the shortest path that visits every node.
# You may start and stop at any node, you may revisit nodes multiple times,
# and you may reuse edges.
#
# Example 1:
#
# Input: [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
# Example 2:
#
# Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
import collections


'''
지금까지 풀었던 다른 문제들과 약간 다른 부분: All Nodes!
    Even if we have visited a node, we could have a different result by 
    visiting nodes in a different sequence...!
'''


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # Keep a tuple (visited_so_far, source) such that
        #   source is from any of the visited_so_far.
        # Then, try visiting from the source to all target.
        # We are done when visited_so_far == all possible nodes
        len_graph = len(graph)
        distance_visited = collections.defaultdict(lambda: len_graph ** 2)
        queue = collections.deque((1 << node_idx, node_idx) for node_idx in range(len_graph))

        # Initialize identity distances
        for node_idx in range(len_graph):
            distance_visited[1 << node_idx, node_idx] = 0

        while queue:
            visited, node_idx = queue.popleft()
            current_distance = distance_visited[visited, node_idx]

            if visited == (1 << len_graph) - 1:
                return current_distance

            for target_idx in graph[node_idx]:

                with_the_target = visited | (1 << target_idx)

                if current_distance + 1 < distance_visited[with_the_target, target_idx]:
                    distance_visited[with_the_target, target_idx] = current_distance + 1
                    queue.append((with_the_target, target_idx))


