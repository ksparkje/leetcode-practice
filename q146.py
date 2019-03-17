from collections import OrderedDict


class Node:
    def __init__(self, key, val, prev, n):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = n

'''
Doubly Linked List with Front and Back as default!

[FrontNode] <=> [Node1] <=> [Node2] <=> ... <=> [BackNode]

dictionary with key: NodeX
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.front = Node(-1, -1, None, None)
        self.back = Node(-1, -1, None, None)

        self.front.next, self.back.prev = self.back, self.front

        # dict with key -> Node
        self.dict = dict()

    def pop_from_the_linked_list(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.dict.pop(node.key)

    def put_in_the_back(self, node):
        prev = self.back.prev
        prev.next = node
        node.prev = prev
        node.next = self.back
        self.back.prev = node
        self.dict[node.key] = node

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.pop_from_the_linked_list(node)
            self.put_in_the_back(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self.pop_from_the_linked_list(node)

        self.put_in_the_back(Node(key, value, None, None))

        if len(self.dict) > self.capacity:
            self.pop_from_the_linked_list(self.front.next)


class LRUCache:
    '''
    defeats the purpose... a terrible idea...
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        val = self.dict.get(key, None)
        if val:
            self.dict.pop(key)
            self.dict[key] = val
        return val if val else -1

    def put(self, key: int, value: int) -> None:
        val = self.dict.get(key, None)
        if val:
            self.dict.pop(key)

        self.dict[key] = value

        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)