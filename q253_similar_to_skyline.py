# # 253. Meeting Rooms II
# # Medium
# #
# # Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# #
# # Example 1:
# #
# # Input: [[0, 30],[5, 10],[15, 20]]
# # Output: 2
# # Example 2:
# #
# # Input: [[7,10],[2,4]]
# # Output: 1
#
#
# # Definition for an interval.
import heapq


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
'''
o -------------- o
        o ------ o
              o ------ o
                    o ----- o

When we go to next starting point,
    while current starting point >= current ending point:
        unlock those no-longer used rooms
    use one of the rooms

This idea is very similar to that of skyline problem!
'''
class Solution:
    def minMeetingRoomsMyBest(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        max_count = 0

        intervals.sort(key=lambda x: (x.start, x.end))
        queue = []

        for cur in intervals:
            start = cur.start
            end = cur.end

            while queue and start >= queue[0]:
                heapq.heappop(queue)

            heapq.heappush(queue, end)

            max_count = max(max_count, len(queue))

        return max_count

    def minMeetingRoomsFromDiscussion(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        s = sorted([i.start for i in intervals])
        e = sorted([i.end for i in intervals])

        start_idx = 0
        end_idx = 0

        total_rooms = available_rooms = 0

        while start_idx < len(intervals):

            # I need to find a room
            if s[start_idx] < e[end_idx]:

                if available_rooms:
                    available_rooms -= 1
                else:
                    total_rooms += 1

                start_idx += 1

            # I can return the room being used
            else:
                available_rooms += 1
                end_idx += 1

        return total_rooms

    def minMeetingRoomsBetter(self, intervals):
        intervals.sort(key=lambda x: x.start)
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i.start >= heap[0]:
                # means two intervals can use the same room
                # heapreplace pops first, then push, (differ from heappushpop)
                heapq.heapreplace(heap, i.end)
            else:
                # a new room is allocated
                heapq.heappush(heap, i.end)
        return len(heap)















