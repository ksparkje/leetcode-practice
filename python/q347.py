# 347. Top K Frequent Elements
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
from collections import Counter
from itertools import islice
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        by_freq = [(freq, key) for key, freq in counter.items()]

        first_k_values = list(islice(by_freq, k))
        heapq.heapify(first_k_values)

        for freq, key in by_freq[k:]:
            heapq.heappushpop(first_k_values, (freq, key))

        return [key for freq, key in first_k_values]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))


