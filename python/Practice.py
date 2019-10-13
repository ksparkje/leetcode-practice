class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.center = None
        self.right = None

    def __str__(self):
        return str(self.val)


t = TreeNode(2)

left_t = TreeNode(3)
t.left = left_t

left_left_t = TreeNode(10)
left_t.left = left_left_t

right_t = TreeNode(4)
t.right = right_t

right_right_t = TreeNode(11)
right_t.right = right_right_t

stack = [[t.left, t.right]]
print(stack)

def printMyTree(given_tree_node):
    queue = [given_tree_node]
    while queue:
        cur_item = queue.pop(0)
        if cur_item.left:
            queue.append(cur_item.left)
        if cur_item.right:
            queue.append(cur_item.right)

    #    if cur_item.left == cur_item.right: return True
    #    if cur_item.left != cur_item.right: return False
        print(cur_item)
printMyTree(t)