# 236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            '''
            :param node: current node
            :return: tuple (count_of_found, node_if_found)
            '''
            if not node:
                return 0, None

            left_result = dfs(node.left)
            if left_result[1]:
                return left_result

            right_result = dfs(node.right)
            if right_result[1]:
                return right_result

            total_count = 1*(node.val in (p.val, q.val)) + left_result[0] + right_result[0]

            return (total_count, node) if total_count == 2 else (total_count, None)

        return dfs(root)[1]


