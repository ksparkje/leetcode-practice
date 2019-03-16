# 298. Binary Tree Longest Consecutive Sequence
#
# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in the
# tree along the parent-child connections. The longest consecutive path need to be from
# parent to child (cannot be the reverse).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        def check_myself_left_right(node, cur_max):
            '''
            :param node: current node
            :param cur_max: max_consecutive upto this node
            :return: max consecutive node in all path
            '''

            if not node:
                return cur_max

            left_result = (check_myself_left_right(node.left, cur_max + 1)
                           if node.left and node.left.val == node.val + 1
                           else cur_max if not node.left else check_myself_left_right(node.left, 1))

            right_result = (check_myself_left_right(node.right, cur_max + 1)
                            if node.right and node.right.val == node.val + 1
                            else cur_max if not node.right else check_myself_left_right(node.right, 1))

            return max(cur_max, left_result, right_result)

        return check_myself_left_right(root, 1)




