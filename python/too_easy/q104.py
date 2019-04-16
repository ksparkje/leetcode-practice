# 104. Maximum Depth of Binary Tree
# Easy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return (0 if not root
                else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))

