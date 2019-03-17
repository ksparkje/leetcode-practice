# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '{},'.format(self.val)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(cur_node):
            if not cur_node:
                return 'None,'
            to_return = str(cur_node.val) + ','
            left_sub_tree = dfs(cur_node.left)
            right_sub_tree = dfs(cur_node.right)
            return to_return + left_sub_tree + right_sub_tree

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == 'None,':
            return None

        def build_tree(tree_list, idx):
            if tree_list[idx] is None:
                return None, idx
            else:
                cur_node = TreeNode(tree_list[idx])
                cur_node.left, idx = build_tree(tree_list, idx+1)
                cur_node.right, idx = build_tree(tree_list, idx+1)
                return cur_node, idx

        nodes_in_list = [eval(item) for item in data.split(',')[:-1]]
        tree_head, _ = build_tree(nodes_in_list, 0)
        return tree_head

    def deserialize(self, data):
        """
        From Official answer key...
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# by zjlvmiao
#
# BFS with Queue
class Codec:
    '''       O(n) time and O(n) space, BFS traversal
    e.g., 1
         / \
        2   5
       / \
      3   4  , level order traversal, serialize will be '1,2,5,3,4,None,None,None,None,None,None,'; deserialize
      with queue as well, convert back. Time and Space O(n).
    '''

    def serialize(self, root):
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        res = ''
        while queue:
            node = queue.popleft()
            if not node:
                res += 'None,'
                continue
            res += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        return res

    def deserialize(self, data):
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(int(ls[0]))
        queue = collections.deque()
        queue.append(root)
        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != 'None':
                left = TreeNode(int(ls[i]))
                node.left = left
                queue.append(left)
            i += 1
            if ls[i] != 'None':
                right = TreeNode(int(ls[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root




def build_tree(tree_list, idx):
    if tree_list[idx] is None:
        return None, idx
    else:
        cur_node = TreeNode(tree_list[idx])
        cur_node.left, idx = build_tree(tree_list, idx+1)
        cur_node.right, idx = build_tree(tree_list, idx+1)
        return cur_node, idx


def print_tree_preorder(tree_node):
    if not tree_node:
        return
    print(tree_node)
    print_tree_preorder(tree_node.left)
    print_tree_preorder(tree_node.right)


if __name__ == '__main__':
    tree = [-1,0,1]
    tree_head, _ = build_tree(tree, 0)

    print_tree_preorder(tree_head)

    s = Codec()
    print([eval(item) for item in s.serialize(tree_head).split(',')[:-1]])

