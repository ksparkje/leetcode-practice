# 199. Binary Tree Right Side View
#
# Given a binary tree, imagine yourself standing on the right side of it, return the
# values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        view_from_the_top = []
        this_row = [root]
        while this_row:
            view_from_the_top.append(this_row[-1].val)
            this_row = [child
                        for node in this_row
                        for child in (node.left, node.right) if child]

        return view_from_the_top


