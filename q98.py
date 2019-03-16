# 98. Validate Binary Search Tree

# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# 쉬워보이지만 착각하면 말리는 문제
# BST는 search 이므로 left, right을 줄여간다는 생각과 시작은 -inf, inf 로 ...

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check_node(node, min_val, max_val):
            if not node:
                return True
            if not min_val <= node.val <= max_val:
                return False
            # 이게 방점...
            return (check_node(node.left, min_val, node.val) and
                    check_node(node.right, node.val, max_val))

        inf = float('inf')
        return check_node(root, -inf, inf)
