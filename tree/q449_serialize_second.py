# 449. Serialize and Deserialize BST
# Medium
#
# Serialization is the process of converting a data structure or object into a sequence of
# bits so that it can be stored in a file or memory buffer, or transmitted across a network
# connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction
# on how your serialization/deserialization algorithm should work. You just need to ensure that a
# binary search tree can be serialized to a string and this string can be deserialized to the
# original tree structure.
#
# The encoded string should be as compact as possible.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and
# deserialize algorithms should be stateless.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
나 자신을 먼저 찍고, 왼쪽으로 가고 오른쪽으로 가고, None 인 경우는 무조건 None을 리턴해줘라!
이래야 디시리얼라이징이 쉽다!
'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        so_far = []

        def dfs(node):
            if not node:
                so_far.append('None')
                return
            # BEST TO DO IT IN PREODER!!!
            so_far.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ','.join(so_far)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def create_tree(node_list):
            # return me the first node which is connected to all the rest
            first_elem_val = node_list.pop(0)
            if first_elem_val == 'None':
                return None
            cur_node = TreeNode(first_elem_val)
            cur_node.left = create_tree(node_list)
            cur_node.right = create_tree(node_list)
            return cur_node

        split = data.split(',')
        root = create_tree(split)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

