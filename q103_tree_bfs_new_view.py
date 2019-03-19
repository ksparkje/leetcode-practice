# 103. Binary Tree Zigzag Level Order Traversal
# Medium
#
# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        this_row, so_far, direction = [root], [], 1

        while this_row:

            this_row_values = [node.val for node in this_row][::direction]
            so_far += [this_row_values]

            direction *= -1

            # 완전 쉽지만 (뭐 그걸 누가 모르냐) 발상의 전환!!!
            # update this_row
            this_row = [child
                        for node in this_row
                        for child in (node.left, node.right) if child]

        return so_far
