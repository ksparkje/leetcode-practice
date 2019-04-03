# 56. Merge Intervals
# Medium
#
# Given a collection of intervals, merge all overlapping intervals.

# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
from typing import List


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str((self.start, self.end))


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        out = []

        for item in sorted(intervals, key=lambda x: x.start):
            if out and item.start <= out[-1].end:
                out[-1].end = max(out[-1].end, item.end)
            else:
                out += [item]
        return out


