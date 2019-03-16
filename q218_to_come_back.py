# 218. The Skyline Problem

# For instance, the dimensions of all buildings in Figure A are recorded as:
# [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
#
# The output is a list of "key points" (red dots in Figure B) in the format of
# [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline.
# A key point is the left endpoint of a horizontal line segment.
# Note that the last key point, where the rightmost building ends,
# is merely used to mark the termination of the skyline, and always has zero height.
# Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.
#
# For instance, the skyline in Figure B should be represented as:
# [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
#
# Notes:
#
# The number of buildings in any input list is guaranteed to be in the range [0, 10000].
# The input list is already sorted in ascending order by the left x position Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height in the output skyline. For instance,
# [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable;
# the three lines of height 5 should be merged into one in the final output as such:
# [...[2 3], [4 5], [12 7], ...]

# 까다로움... 좋은 문제
from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        # negative height is crucial! Must be done here!
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))] # float(inf) represents the ending point in x axis, not height!
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            while live[0][1] <= pos: # live[0][1] is position_x for the right
                heappop(live)
            # 2, if it's the start-building event, make the building alive
            if negH:
                heappush(live, (negH, R))

            # 여기 밑줄 쫙!
            # 3, if previous keypoint height != current highest height, edit the result
            if res[-1][1] != -live[0][0]:
                res += [[pos, -live[0][0]]]
        return res[1:]
