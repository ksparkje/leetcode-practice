# 895. Maximum Frequency Stack
# Hard
#
# Implement FreqStack, a class which simulates the operation of a stack-like data structure.
#
# FreqStack has two functions:
#
# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the stack.
# If there is a tie for most frequent element, the element closest to the
# top of the stack is removed and returned.

'''
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],            [5],   [7],   [5],   [7],   [4],   [5],   [],   [],   [],   []]
Output: [null, null,  null,  null,  null,  null,  null,    5,    7,    5,    4]

Need to have a sorted list by frequency

5: 1
7: 1
5: 2
7: 2
4: 1
5: 3 -> try it on max_heap?

Here is what I mean:
    Keep a max_heap.

    push: keep a dictionary, telling how many x exists so far.
          push the (count+1, x) into the heap
          Since it's max heap, we actually do the inverse, count - 1

    pop: pop the (count, x), return x
         decrease the counter

'''
from heapq import *
from collections import defaultdict, Counter


class FreqStack:

    def __init__(self):
        self.counter = defaultdict(int)
        self.max_heap = []

    def push(self, x: int) -> None:
        x_count = self.counter[x]
        heappush(self.max_heap, (x_count-1, x))
        self.counter[x] -= 1

    def pop(self) -> int:
        counts, popped = heappop(self.max_heap)
        self.counter[popped] += 1
        return popped


'''
Discussion Solution, with O(1)

For each x, keep frequency... Use Counter
For each frequency, keep a list of such elem remaining.
`Best` holds the current highest freq
'''
class FreqStack:
    def __init__(self):
        self.most_count = 0
        self.x_counter = defaultdict(int)
        self.freq_to_x_list = defaultdict(list)

    def push(self, x):
        self.x_counter[x] = x_count = self.x_counter[x] + 1
        self.freq_to_x_list[x_count] += [x]
        self.most_count = max(self.most_count, x_count)

    def pop(self):
        most_count_item = self.freq_to_x_list[self.most_count].pop()
        if not self.freq_to_x_list[self.most_count]:
            self.most_count -= 1
        self.x_counter[most_count_item] -= 1
        return most_count_item


























