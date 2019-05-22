# 138. Copy List with Random Pointer
# Medium
#
# A linked list is given such that each node contains an additional
# random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.

# ARTICLE EXISTS...
# https://leetcode.com/articles/copy-list-with-random-pointer/
from collections import defaultdict


# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def __hash__(self):
        return hash(id(self))


class Solution:
    '''
    Use dictionary to hash each Node
    Try dfs on each node
    Inspired by: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43484/C%2B%2B-6-lines-recursive-solution-using-memoization
    '''
    def copyRandomList(self, head: Node):
        def dfs(node: Node):
            '''
            :param node:
            :return: a new Node corresponding to the node if in so_far
            '''
            if not node:
                return None

            if node in so_far:
                return so_far.get(node)

            else:
                so_far[node].val = node.val
                so_far[node].next = dfs(node.next)
                so_far[node].random = dfs(node.random)
                return so_far[node]

        so_far = defaultdict(lambda: Node(None, None, None))
        return dfs(head)


class Solution(object):
    '''
    Use dictionary to hash each Node
    '''
    def copyRandomList(self, head):

        if not head:
            return None

        m = n = head
        # THIS IS SUPER INTERESTING...
        original_to_copy = defaultdict(lambda: Node(0, None, None))

        while m:
            original_to_copy[m].val = m.val
            m = m.next

        while n:
            original_to_copy[n].next = original_to_copy.get(n.next)
            original_to_copy[n].random = original_to_copy.get(n.random)
            n = n.next

        return original_to_copy[head]


'''
ELEGANT WAY OF USING ITERATOR
http://www.cnblogs.com/zuoyuan/p/3745126.html

Problem-solving ideas: This question mainly requires deep copying. 
Look at the picture to understand how to write the program.

-------------------------------------
|                                   |
1 -> [1](copy) -> 2 -> [2](copy) -> 3 -> [3](copy) -> 4 -> [4](copy) -> None
                  |                                   |
                  -------------------------------------

First, a new node is inserted after each node of the original list. 
The content of the new node is the same as the previous node. 
For example, the above picture, insert 1 after 2, insert 2 after, and so on.

Second, how do the random pointers in the original list map? 
For example, in the above figure, the 1 node's random pointer points to 3, 
and the 4 node's random pointer points to 2. If there is a tmp pointer 
pointing to 1 (blue), then a statement: tmp.next.random = tmp.random.next; 
can solve this problem.

The third step is to split the new linked list from the linked list above.

https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43689/Python-solution-without-using-dictionary.
'''


'''
Create a copy of next pointer first, then copy myself.
Don't worry about the random at first. Do a second traversal.
'''
class SolutionMine(object):
    # This is shit horrible answer...
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        def dfs(cur_node):
            '''
            :param cur_node:
            :return: next_node created by copy, which can be used as a next pointer of current node's copy
            '''
            if not cur_node:
                return

            next_node_copied = dfs(cur_node.next) if cur_node.next else None

            return Node(cur_node.val, next_node_copied, None)

        def count_to_the_end(cur_node, so_far):
            if not cur_node:
                return so_far
            return count_to_the_end(cur_node.next, so_far+1)

        def get_length_of_whole_list(node):
            if not node:
                return 0
            return 1 + get_length_of_whole_list(node.next)

        whole_length_list = get_length_of_whole_list(head)

        copied_list_without_random = dfs(head)

        orig, copy = head, copied_list_without_random

        while orig and copy:
            assert orig.val == copy.val, '{} vs {}'.format(orig.val, copy.val)

            dist_to_next_random = count_to_the_end(orig.random, 1)
            num_from_beg = whole_length_list - dist_to_next_random

            temp = copied_list_without_random
            for _ in range(num_from_beg):
                temp = temp.next

            copy.random = temp

            orig = orig.next
            copy = copy.next

        return copied_list_without_random













