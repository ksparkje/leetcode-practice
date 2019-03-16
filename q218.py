from heapq import heappush, heappop


class Solution(object):
    def getSkyline(self, buildings):

        if not buildings:
            return []

        all_points = []
        for beg, end, height in sorted(buildings, key=lambda x: x[0]):
            # -height must be done here, to purposely sort the list
            # and have highest height come before!
            all_points.append((beg, -height, end))
            all_points.append((end, 0, 0))

        all_points.sort()

        last_building_point = all_points[-1][0]

        # pq is max_heap with -height, ending_point
        pq = [(0, last_building_point+1)]
        # ret: position, height
        ret = [(0, 0)]

        for point, neg_height, end in all_points:
            # get rid of no longer valid points while they are in the front of the queue
            while pq[0][1] <= point:
                heappop(pq)
            if neg_height:
                heappush(pq, (neg_height, end))
            if ret[-1][1] != -pq[0][0]:
                ret.append((point, -pq[0][0]))

        return ret[1:]


if __name__ == '__main__':
    s = Solution()
    # buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    buildings = [[0,2,3], [2,5,3]]
    buildings = [[1,2,1],[1,2,2],[1,2,3]]
    print(s.getSkyline(buildings))