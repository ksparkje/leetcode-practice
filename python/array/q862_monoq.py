# 862. Shortest Subarray with Sum at Least K

# Return the length of the shortest, non-empty,
# contiguous subarray of A with sum at least K.
#
# If there is no non-empty subarray with sum at least K, return -1.
#
# Example 1:
#
# Input: A = [1], K = 1
# Output: 1

# Example 2:
#
# Input: A = [1,2], K = 4
# Output: -1

# Example 3:
#
# Input: A = [2,-1,2], K = 3
# Output: 3
from typing import List
import collections
from itertools import accumulate


class Solution2(object):
    def shortestSubarray(self, A, K):
        p = list(accumulate([0] + A))
        # Let's keep a monoq
        # monoq = []
        monoq = collections.deque()
        min_dist = impossible = len(A) + 1

        for idx, py in enumerate(p):
            while monoq and monoq[-1][1] >= py:
                monoq.pop()

            while monoq and py - monoq[0][1] >= K:
                min_dist = min(min_dist, idx - monoq[0][0])
                monoq.popleft()

            monoq.append([idx, py])

        return min_dist if min_dist != impossible else -1


'''
This is brilliant question with actual monotonic queue.
'''
# From official solution
class Solution(object):
    def shortestSubarray(self, A, K):
        N = len(A)
        # First zero is appended to take care of a case where
        # the first element is larger than K...
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        # Want smallest y-x with Py - Px >= K
        ans = N+1   # N+1 is impossible
        monoq = collections.deque()     # opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            # Want opt(y) = largest x with Px <= Py - K

            # Notice, this part would not exist if all elements in A was positive.
            # Because, P will be already monotonically increasing.
            while monoq and Py <= P[monoq[-1]]:
                # If the last elem in monoq was able to make partial sum
                # get larger than K, that computation would have been
                # done by the previous loop...
                print('Before pop right: {}'.format(monoq))
                monoq.pop()

            # monoq[0] is the minimum of the current possible
            # and it can be negative!
            # Therefore, Py - P[monoq[0]] = Py - minimum is the
            # best, or max, I can do right now!
            while monoq and Py - P[monoq[0]] >= K:
                print('Before poping left : {}'.format(monoq))
                ans = min(ans, y - monoq.popleft())
                print('Ans: {}'.format(ans))

            monoq.append(y)
            print('After appending: {}'.format(monoq))
            print('** Current interest : {}'.format(P[monoq[0]:y+1]))

        return ans if ans < N+1 else -1


if __name__ == '__main__':

    A = [1, 2, -2, -2, 1, 2, 1, 3]
    K = 4

    s = Solution2()
    print(s.shortestSubarray(A, K))



