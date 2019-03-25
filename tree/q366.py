# 366. Find Leaves of Binary Tree
#
# Given a binary tree, collect a tree's nodes as if you were doing this:
# Collect and remove all leaves, repeat until the tree is empty.
#
# Example:
#
# Input: [1,2,3,4,5]
#
#           1
#          / \
#         2   3
#        / \
#       4   5
#
# Output: [[4,5,3],[2],[1]]
#
#
# Explanation:
#
# 1. Removing the leaves [4,5,3] would result in this tree:
#
#           1
#          /
#         2
#
#
# 2. Now removing the leaf [2] would result in this tree:
#
#           1
#
#
# 3. Now removing the leaf [1] would result in the empty tree:
#
#           []


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        so_far = [[]]

        def dfs(node):
            if not node:
                return -1
            if not node.left and not node.right:
                so_far[0].append(node.val)
                return 0
            depth = max(dfs(node.left), dfs(node.right)) + 1

            if len(so_far) <= depth:
                so_far.append([])
            so_far[depth].append(node.val)
            return depth

        dfs(root)
        return so_far






