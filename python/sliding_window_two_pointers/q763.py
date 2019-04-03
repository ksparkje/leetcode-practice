# 763. Partition Labels
# Medium
#
# A string S of lowercase letters is given. We want to partition this string into as
# many parts as possible so that each letter appears in at most one part, and return a
# list of integers representing the size of these parts.
#
# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        start_end = dict()

        for idx, c in enumerate(S):
            if c not in start_end:
                start_end[c] = [idx, idx]
            else:
                start_end[c][-1] = idx

        so_far = []
        for start, end in sorted(start_end.values()):
            if not so_far:
                so_far.append([start, end])
            else:
                if start > so_far[-1][-1]:
                    so_far.append([start, end])
                else:
                    so_far[-1][-1] = max(end, so_far[-1][-1])
        return [end - start + 1 for start, end in so_far]

