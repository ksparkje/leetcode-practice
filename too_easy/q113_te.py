# 113. Path Sum II
# Medium
#
# Given a binary tree and a sum, find all root-to-leaf paths where
# each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        answer = []

        def dfs(node, sum_so_far, path):
            if not node:
                return

            updated_sum = sum_so_far + node.val
            updated_path = path+[node.val]

            if not (node.left or node.right):
                if updated_sum == sum:
                    answer.append(updated_path)
                return


            dfs(node.left, updated_sum, updated_path)
            dfs(node.right, updated_sum, updated_path)

        dfs(root, 0, [])

        return answer
