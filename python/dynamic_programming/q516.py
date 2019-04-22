# 516. Longest Palindromic Subsequence
# Medium

# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input:

# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:

# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".


'''
Interesting question. Notice, the question is about the length!
    bbbab -> b (bba) b
          -> b ( b () b ) b

    abcdedbajjj  -> a (bcdedb) a ---   Both are the same
    abcdedabajjj -> a (bcdedab) a ---

    Find the first elem and the last elem
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def f(remaining: str):
            if len(remaining) <= 1:
                return len(remaining)
            if remaining in visited:
                return visited[remaining]
            max_so_far = 0
            for c in set(remaining):
                left = remaining.find(c)
                right = remaining.rfind(c)

                if left == right:
                    rest = 1
                else:
                    rest = f(remaining[left + 1: right]) + 2

                max_so_far = max(max_so_far, rest)

            visited[remaining] = max_so_far
            return max_so_far

        visited = {}
        return f(s)


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindromeSubseq('abcdedbajjj'))










