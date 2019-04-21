# 992. Subarrays with K Different Integers
# Hard
#
# Given an array A of positive integers, call a (contiguous, not necessarily distinct)
# subarray of A good if the number of different integers in that subarray is exactly K.
#
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
#
# Return the number of good subarrays of A.
#
#
# Example 1:
#
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers:
# [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
# Example 2:
#
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers:
# [1,2,1,3], [2,1,3], [1,3,4].
from typing import List
import collections


'''
1. I need a tracker to know which elems are in the subarray.
    - dictionary to keep track of the number of elements

A = [1, 2, 1, 2, 1, 2, 3, 4], K = 3
If I keep k==3 distinct and k==2 distinct window
idx  0  1  2  3  4  5  6
    [1, 2, 1, 2, 1, 2, 3] k == 3
    [-, -, -, -, -, 2, 3] k == 2
The number of subarray with exactly 3 different integers is 5 - 0 = 5

idx  0  1  2  3  4  5  6  7
    [-, -, -, -, -, 2, 3, 4] k == 3
    [-, -, -, -, -, -, 3, 4] k == 2
The number of subarray with exactly 3 different integers is 6 - 5 = 1


Good explanation + implementation
https://leetcode.com/articles/subarrays-with-k-different-integers/
'''
class Distinct:
    def __init__(self):
        self.k = 0
        self.counter = collections.Counter()

    def add(self, item):
        self.counter[item] += 1
        if self.counter[item] == 1:
            self.k += 1

    def remove(self, item):
        self.counter[item] -= 1
        if self.counter[item] == 0:
            self.k -= 1


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        distinct_one_less = Distinct()
        distinct = Distinct()

        count = left_one_less = left = 0

        for right, item in enumerate(A):
            distinct.add(item)
            distinct_one_less.add(item)

            # This should be done in the class method, but A's info
            # is not given, so that's why we're doing it here
            while distinct.k > K:
                distinct.remove(A[left])
                left += 1

            while distinct_one_less.k > K - 1:
                distinct_one_less.remove(A[left_one_less])
                left_one_less += 1

            count += left_one_less - left

        return count


'''
Not intuitive solution...
https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/234482/JavaC%2B%2BPython-Sliding-Window-with-Video
'''
class Solution2:
    def subarraysWithKDistinct(self, A, K):
        return atMostK(A, K) - atMostK(A, K - 1)

def atMostK(A, K):
    count = collections.Counter()
    res = i = 0
    for j in range(len(A)):
        if count[A[j]] == 0:
            # read a new integer, reduce K by 1 for each newly added integer,
            # when K is -1, you cannot add more integers
            K -= 1
        count[A[j]] += 1 #count new entry
        # No new integers should be added, will need to move the left pointer before adding new ones
        while K == -1:
            count[A[i]] -= 1
            if count[A[i]] == 0:  #successfully cut down an old integer
                K += 1
            i += 1 # move left pointer

        # A[i,j+1] is the longest subarray with right end A[j+1] which has at most K distinct integers,
        # so the number of such subarrays which ends with A[j] is j-i+1
        res += j - i + 1
    return res






















