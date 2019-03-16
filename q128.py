# 128. Longest Consecutive Sequence

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        visited = {}
        graph = set(nums)

        for node in graph:
            if node not in visited:
                count = 0
                queue = [node]

                while queue:
                    cur_node = queue.pop(0)
                    if cur_node in graph and cur_node not in visited:
                        count += 1
                        visited[cur_node] = count
                        for next_node in [cur_node + 1, cur_node - 1]:
                            queue.append(next_node)
                visited[node] = count

        return max(visited.values())

if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([1,3,4, 20, 23, 22, 25,24, 26, 102, 100]))




