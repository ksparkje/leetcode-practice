# 865. Smallest Subtree with all the Deepest Nodes

# Given a binary tree rooted at root, the depth of each node is the shortest
# distance to the root.
#
# A node is deepest if it has the largest depth possible among any node in the
# entire tree.
#
# The subtree of a node is that node, plus the set of all descendants of that node.
#
# Return the node with the largest depth such that it contains all the deepest nodes
# in its subtree.
#
# Example 1:
#
# Input: [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation:
#
#
#
# We return the node with value 2, colored in yellow in the diagram.
# The nodes colored in blue are the deepest nodes of the tree.
# The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
# The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
# Both the input and output have TreeNode type.
#
#
# Note:
#
# The number of nodes in the tree will be between 1 and 500.
# The values of each node are unique.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def compute_depth(node):
            if not node:
                return 0, None
            if node.left is None and node.right is None:
                return 1, node

            # left node and right node corresponds to the deepest subtree nodes
            left_subtree_depth, left_node = compute_depth(node.left)
            right_subtree_depth, right_node = compute_depth(node.right)

            if left_subtree_depth == right_subtree_depth:
                return left_subtree_depth + 1, node
            else:
                if left_subtree_depth > right_subtree_depth:
                    return left_subtree_depth + 1, left_node
                else:
                    return right_subtree_depth + 1, right_node

        return compute_depth(root)[1]











