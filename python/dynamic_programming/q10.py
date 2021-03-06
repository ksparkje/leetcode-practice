# 10. Regular Expression Matching
# Hard
#
# Given an input string (s) and a pattern (p), implement regular expression matching
# with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a'
# once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:

        visited = {}

        def dp(i, j):
            if (i, j) not in visited:
                if j == len(p):
                    ret = i == len(s)
                else:
                    char_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ret = (char_match and dp(i+1, j)) or dp(i, j+2)
                    else:
                        ret = char_match and dp(i+1, j+1)

                visited[i, j] = ret

            return visited[i, j]

        return dp(0, 0)


class Solution:
    def isMatchNonDP(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_char_same = bool(s) and (s[0] == p[0] or p[0] == '.')

        if len(p) >= 2 and p[1] == '*':
            return (first_char_same and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        else:
            return first_char_same and self.isMatch(s[1:], p[1:])

    def isMatch(self, s: str, p: str) -> bool:
        so_far = {}

        def dp(i, j):

            if (i, j) not in so_far:
                if j == len(p):
                    ret = i == len(s)
                else:
                    first_char_equal = i < len(s) and (s[i] == p[j] or p[j] == '.')
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ret = (first_char_equal and dp(i + 1, j)) or dp(i, j + 2)
                    else:
                        ret = first_char_equal and dp(i + 1, j + 1)

                so_far[i, j] = ret

            return so_far[i, j]

        return dp(0, 0)

    def isMatch(self, s: str, p: str) -> bool:
        s = '_' + s
        p = '_' + p

        len_s = len(s)
        len_p = len(p)

        dp = [[False]*len_p for _ in range(len_s)]

        dp[0][0] = True
        for idx in range(1, len_p):
            if p[idx] == '*':
                dp[0][idx] = dp[0][idx-2]

        for i in range(1, len_s):
            for j in range(1, len_p):
                if p[j] == '*':
                    without_star = dp[i][j-2]
                    with_star = (s[i] == p[j-1] or p[j-1] == '.') and dp[i-1][j]
                    #                                               Not necessary b/c '*'
                    # with_star = (s[i] == p[j-1] or p[j-1] == '.') and any((dp[i-1][j-2],
                    #                                                        dp[i-1][j]))
                    ret = with_star or without_star
                else:
                    ret = dp[i-1][j-1] and (s[i] == p[j] or p[j] == '.')

                dp[i][j] = ret

        return dp[len_s-1][len_p-1]




















if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('aa', 'a*'))