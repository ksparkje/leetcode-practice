# 543. Diameter of Binary Tree
#
# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
easy로 돼 있지만 생각을 요함...
'''
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0, -1
            if not node.left and not node.right:
                return 0, 0
            left_sub_tree_best, left_depth = dfs(node.left)
            right_sub_tree_best, right_depth = dfs(node.right)

            # +2 를 하고싶으면 leaf depth == 0
            this_node_max_dist = left_depth + right_depth + 2
            return (max(left_sub_tree_best, right_sub_tree_best, this_node_max_dist),
                    max(left_depth, right_depth) + 1)

        return max(dfs(root))



