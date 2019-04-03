# 44. Wildcard matching
# Given an input string (s) and a pattern (p), implement wildcard pattern matching
# with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).


class Solution:
    so_far = {}
    def isMatch(self, s: str, p: str) -> bool:
        # DO NOT CACHE WITH s+p THIS CAUSES ERROR YOU STUPID
        if (s, p) in self.so_far:
            return self.so_far[s, p]

        if not s:
            # not > and > or
            return not p or p == '*' * len(p)
        if not p:
            return False

        if p[0] == '?':
            ret = self.isMatch(s[1:], p[1:])
        elif p[0] == '*':
            ret = self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
        else:
            ret = s[0] == p[0] and self.isMatch(s[1:], p[1:])

        self.so_far[s, p] = ret

        return ret


class Solution2:
    def is_match(self, s, p):
        s = '_' + s
        p = '_' + p
        len_i, len_j = len(s), len(p)

        table = [[False] * len_j for _ in range(len_i)]
        table[0][0] = True

        for j in range(1, len_j):
            if p[j] == '*':
                table[0][j] = table[0][j-1]

        for i in range(1, len_i):
            for j in range(1, len_j):
                cur_char = s[i]
                cur_pattern = p[j]

                if cur_pattern == '*':
                    table[i][j] = table[i][j-1] or table[i-1][j]

                elif cur_pattern == '?':
                    table[i][j] = table[i-1][j-1]

                else:
                    table[i][j] = cur_char == cur_pattern and table[i-1][j-1]

        return table[len_i-1][len_j-1]


if __name__ == '__main__':
    s = Solution()
    examples = [('abc', '*'),
                ('abcb', 'a*'),
                ('ho', '**ho'),
                ('bjkeikd', 'b?ke*'),
                ('ferwkk', '*kk'),
                ('cde', '???*'),
                ('ciiide', 'i?*'), # False
                ('acer', 'i?*'), # False
                ('biiide', 'i?*'), # False
                ('a', 'ab*'), # False
            ]

    for given_str, pattern in examples:
        print(s.isMatch(given_str, pattern))
