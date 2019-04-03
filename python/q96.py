# 96. Unique Binary Search Trees
# Medium
#
# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# DP problem
# With [1, 2, 3] => use one of the element as a middle node
# (node_myself, number_of_node_on_left_subtree, number_of_node_on_right_subtree)
# (1, 2, 0), (1, 1, 1), (1, 0, 2)
# i.e. Count all possible combo by left_count * right_count
# [1, 2, 3, 4] => (1, 3, 0), (1, 2, 1), (1, 1, 2), (1, 0, 3)
class Solution:
    def numTrees(self, n: int) -> int:

        so_far = {}

        for i in range(n+1):
            if i in (0, 1):
                so_far[i] = 1
            else:
                temp = 0
                for left in range(i):
                    temp += so_far[left] * so_far[i-1-left]
                so_far[i] = temp

        return so_far[n]

