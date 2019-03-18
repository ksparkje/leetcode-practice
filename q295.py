# 295. Find Median from Data Stream
# Hard
#
# Median is the middle value in an ordered integer list. If the size of the list is
# even, there is no middle value. So the median is the mean of the two middle value.
#
# For example,
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.


'''
[2, 3, 4]
[2, 3] , [4]

[2, 3, 4, 5]
[2, 3], [4, 5]

[2, 3, 4, 5, 6, 10, 12]
[2, 3, 4, 5], [6, 10, 12]

must be sorted, left and right

add number:
if len(left) == len(right):
    add to left -> get the min of (cur_num, right)
    add remaining
else: # left > right
    add to right -> get the max of (cur_num, left)
    add remaining

find median:
if len(left) > len(right):
    return last elem of left
else:
    avg of max left, min right

left -> max_heap
right -> min_heap
'''
import heapq
from bisect import insort

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        insort(self.arr, num)

    def findMedian(self):
        """
        :rtype: float
        """
        len_arr = len(self.arr)
        return (self.arr[len_arr // 2] + self.arr[~(len_arr // 2)]) / 2



class MedianFinder:

    def __init__(self):
        """
        self.left => max_heap, so push the neg_value
        """
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            add_to_left = heapq.heappushpop(self.right, num)
            heapq.heappush(self.left, -add_to_left)

        else:
            add_to_right = -heapq.heappushpop(self.left, -num)
            heapq.heappush(self.right, add_to_right)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2





# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()