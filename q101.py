# 101. Symmetric Tree
# Easy
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def check_left_right(left, right):
            if None in (left, right):
                return left == right
            else: # both are not None
                return (left.val == right.val and
                        check_left_right(left.right, right.left) and
                        check_left_right(left.left, right.right))

        return check_left_right(root.left, root.right) if root else True
