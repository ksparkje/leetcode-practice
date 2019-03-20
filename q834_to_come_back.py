# 834. Sum of Distances in Tree
# Hard
#
# An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.
#
# The ith edge connects nodes edges[i][0] and edges[i][1] together.
#
# Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.
#
# Example 1:
#
# Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation:
# Here is a diagram of the given tree:
#   0
#  / \
# 1   2
#    /|\
#   3 4 5
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

# SUPER NICE PROBLEM!!!
import collections


'''
Given 0
     / \
    1   2
       /|\
      3 4 5
        
    dist(2,3) + dist(2,4) + dist(2,5) = 3
    dist(0,3) = dist(0,2) + dist(2,3) = 1 + 1 = 2
    dist(0) = dist(0,2)+ dist(2,3) + dist(2,4) + dist(2,5) + number_of_nodes_in_subtree_of_2
              
Given 0
     / \
    1   2
       /|\
      3 4 5
        |
        6
            
    dist(2,3) + dist(2,4) + dist(2,5) = 3
    dist(0,3) = dist(0,2) + dist(2,3) = 1 + 1 = 2
    dist(0) = dist(0,2)+ dist(2,3) + dist(2,4) + dist(2,5) + dist(2,6) + number_of_nodes_in_subtree_of_2
            = dist(0,2)+ dist(2,3) + dist(2,4) + dist(2,5) + 1 + dist(4,6) + number_of_nodes_in_subtree_of_2
            =    1     +    1      +   1       +    1      + 1 +   1       + ...???
    
'''
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)



