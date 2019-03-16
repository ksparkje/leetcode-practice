# 501. Find Mode in Binary Search Tree

# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [root]

        so_far = defaultdict(int)

        while queue:
            cur_node = queue.pop(0)

            so_far[cur_node.val] += 1

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        key_name = []
        count_max = 0
        for key, val in so_far.items():
            if val > count_max:
                count_max = val
                key_name = [key]
            elif val == count_max:
                key_name += [key]

        return key_name
