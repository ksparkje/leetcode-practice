# 129. Sum Root to Leaf Numbers
#
# Example:
#
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:
#
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def so_far(node, sum_so_far):
            if not node:
                return 0

            sum_so_far = sum_so_far * 10 + node.val

            if not (node.left or node.right):
                return sum_so_far

            left_result = so_far(node.left, sum_so_far)
            right_result = so_far(node.right, sum_so_far)
            return left_result + right_result

        return so_far(root, 0)
