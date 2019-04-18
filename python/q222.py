# 222. Count Complete Tree Nodes

# Given a complete binary tree, count the number of nodes.
#
# Note:
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2h nodes inclusive at
# the last level h.
#
# Example:
#
# Input:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# Output: 6

# 0     1
#      / \
# 1   2   3
#    / \  /
# 2  4  5 6


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        null_node_seen = False
        cur_row = [root]
        cur_level = 0
        while cur_row and not null_node_seen:
            cur_level += 1
            next_row = []
            for item in cur_row:
                if None in (item.left, item.right):
                    null_node_seen = True
                if item.left:
                    next_row += [item.left]
                if item.right:
                    next_row += [item.right]
            cur_row = next_row

        return (1 << cur_level) - 1 + len(next_row)



































