# 145. Binary Tree Postorder Traversal
# Hard
#
# Given a binary tree, return the postorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [3,2,1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Follow up: Recursive solution is trivial, could you do it iteratively?
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Keep a stack, push in (node, visited)
        if visited:
            finish up by adding it to the answer
        else:
            push_in (node,       True)
                    (node.right, False)
                    (node.left,  False)
        '''
        if not root:
            return []

        stack = [(root, False)]
        answer = []

        while stack:
            cur_node, visited = stack.pop()
            if cur_node:
                if visited:
                    answer.append(cur_node.val)
                else:
                    stack.append((cur_node,       True))
                    stack.append((cur_node.right, False))
                    stack.append((cur_node.left,  False))

        return answer


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def post_order(node):
            '''
            :param node:
            :return: list of nodes in post order?
            '''
            if not node:
                return []

            left_subtree = post_order(node.left)
            right_subtree = post_order(node.right)

            return left_subtree + right_subtree + [node.val]
        return post_order(root)


