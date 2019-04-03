# 973. K Closest Points to Origin
#
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#
# (Here, the distance between two points on a plane is the Euclidean distance.)
#
# You may return the answer in any order.  The answer is guaranteed to be unique
# (except for the order that it is in.)


'''
Initial impression: priorityQueue?

'''
from heapq import heappush, heappop, heapify, heappushpop
from typing import List
from itertools import islice


class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        # purposely reverse the equality
        return ((self.x ** 2 + self.y ** 2) >= (other.x ** 2 + other.y ** 2))

    def to_list(self):
        return [self.x, self.y]


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        '''
        :param points: stream?
        :param K:
        :return:
        '''

        if not points or len(points) < K:
            return points

        first_k_points = islice(points, K)
        first_k_points = [Star(*coord) for coord in first_k_points]

        heapify(first_k_points)

        for coord in points[K:]:
            cur_star = Star(*coord)
            heappushpop(first_k_points, cur_star)

        return [star.to_list() for star in first_k_points]


if __name__ == '__main__':
    s = Solution()
    input = [[[1,3],[-2,2]], 1]
    print(s.kClosest(*input))







