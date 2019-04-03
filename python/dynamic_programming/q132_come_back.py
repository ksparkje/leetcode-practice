# 132. Palindrome Partitioning II
# Hard
#
# 517
#
# 21
#
# Favorite
#
# Share
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.


'''
Hmm, palindrome building is quite straight forward now...
Suppose I build the usual table. The first row would have
all the information about this sequence.

example
-------
    a   b   a   c   a   b |  a
a   T   F   T   F   F   F |  T

b       T   F   F   F   T |  F

a           T   F   T   F |  F

c               T   F   F |  F

a                   T   F |  T

b                       T |  F

a                         |  T

Suppose we change the string to 'abacab', without 'a' at the end.
Then, the first T from the right side will be 'aba'. So, we cut it there,
then look for the result on 'cab'. First T from the right is 'c'.... so on.

Actually this doesn't work... See below.
This doesn't work because of cases like 'aaabaa': returns 2, true is 1

'''
class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        len_s = len(s)

        table = [[False] * len_s for _ in range(len_s)]
        for i in range(len_s):
            table[i][i] = True

        for i in range(len_s-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True

        for j in range(2, len_s):
            for i in range(0, j-1):
                if table[i+1][j-1] and s[i] == s[j]:
                    table[i][j] = True

        # TLE, need to cache
        def dfs(row_idx, count):
            if row_idx in so_far:
                return so_far[row_idx]

            min_count_so_far = float('inf')
            for idx, boolean in enumerate(table[row_idx][row_idx:], row_idx):
                if boolean:
                    if idx == len_s - 1:
                        return count
                    min_count_so_far = min(min_count_so_far,
                                           dfs(idx+1, count+1))

            return min_count_so_far

        return dfs(0, 0)


# https://leetcode.com/problems/palindrome-partitioning-ii/discuss/202324/Clear-Python-DP-O(n2)-solution
class SolutionDiscussion:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        This can be solved by:

        cut[end] is the minimum of cut[st-1] + 1 (st <= end) if [st, end] is palindrome

        a   b   a   |   c    c
                        st  end
               st-1 |  [st,  end] is palindrome
          cut(st-1) +  1

        """
        n = len(s)
        cut = [0] * n
        pal = [[False] * n for row in range(n)]

        for end in range(n):
            min_cut = end
            for st in range(end + 1):
                if s[st] == s[end] and (end - st <= 2 or pal[st + 1][end - 1]):
                    pal[st][end] = True
                    min_cut = 0 if st == 0 else min(min_cut, cut[st - 1] + 1)
            cut[end] = min_cut

        return cut[n - 1]


# https://leetcode.com/problems/palindrome-partitioning-ii/discuss/221372/Python-Recursive-DP-Top-down-O(n2)
class Solution:

    def helper(self, s, pos, dp, memo):
        if pos == len(s):
            return 0
        if pos in memo:
            return memo[pos]

        num_palindrome = float('inf')
        for i in range(pos, len(s)):
            if dp[pos][i]:
                num_palindrome = min(num_palindrome, 1 + self.helper(s, i + 1, dp, memo))
        memo[pos] = num_palindrome
        return num_palindrome

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False] * len(s) for _ in range(len(s))]

        for end in range(len(s)):
            for st in range(end + 1):
                if s[st] == s[end] and (end - st <= 2 or dp[st + 1][end - 1]):
                    dp[st][end] = True
        return self.helper(s, 0, dp, {}) - 1


if __name__ == '__main__':
    s = Solution()
    i = 'caaabaa'
    print(s.minCut(i))



















