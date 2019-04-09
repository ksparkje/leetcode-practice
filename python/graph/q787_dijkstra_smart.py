# 787. Cheapest Flights Within K Stops
# Medium
#
# There are n cities connected by m flights. Each fight starts from city u
# and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and
# the destination dst, your task is to find the cheapest price from src to
# dst with up to k stops. If there is no such route, output -1.
#
# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.

# Example 2:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
'''
Dijkstra with modification NICE!
https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaPython-Priority-Queue-Solution
'''


from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int,
                          flights: List[List[int]],
                          src: int,
                          dst: int,
                          k: int) -> int:

        graph = defaultdict(dict)
        for u, v, price in flights:
            graph[u][v] = price

        # price, current_city, k-hops
        queue = [(0, src, 0)]
        while queue:
            cur_price, cur_city, cur_k = heapq.heappop(queue)

            if cur_city == dst:
                return cur_price

            # k stop means k + 1 steps
            if cur_k < k + 1:
                for next_city in graph[cur_city]:
                    heapq.heappush(queue,
                                   (cur_price + graph[cur_city][next_city],
                                    next_city,
                                    cur_k + 1))

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findCheapestPrice(3,
                        [[0,1,100],[1,2,100],[0,2,500]],
                        0,
                        2,
                        1))






