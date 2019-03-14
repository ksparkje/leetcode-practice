# 44. Wildcard matching
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
import functools


class Solution:
    so_far = {}

    def isMatch(self, s: str, p: str) -> bool:

        if s+p in self.so_far:
            return self.so_far[s+p]

        len_s, len_p = len(s), len(p)

        if 0 in (len_s, len_p):
            if len_p > 0:
                result = functools.reduce(lambda x, y: x & (y == '*'), p, True)
            else:
                result = len_s == len_p
            return result

        elif p[-1].isalpha():
            result = False if s[-1] != p[-1] else self.isMatch(s[:-1], p[:-1])

        elif p[-1] == '?':
            result = self.isMatch(s[:-1], p[:-1])

        elif p[-1] == '*':
            if len_p == 1:
                return True
            else:
                prev_char = p[-2]
                idx_to_prev_char = ([idx for idx, char in enumerate(s) if char == prev_char] + [len_s]
                                    if prev_char not in ('?', '*') else list(range(len_s)))
                result = any(self.isMatch(s[:idx+1], p[:-1]) for idx in idx_to_prev_char)
        else:
            result = False

        self.so_far[s+p] = result
        return result


class Solution_2:
    def is_match(self, s, p):
        len_s, len_p = len(s), len(p)
        table = [[False] * (len_s + 1) for _ in range(len_p + 1)]
        table[0][0] = True

        for i in range(1, len_p + 1):
            for j in range(1, len_s + 1):
                cur_string = s[j-1]
                cur_pattern = p[i-1]

                if cur_pattern.isalpha():
                    table[i][j] = cur_string == cur_pattern and table[i-1][j-1]

                elif cur_pattern == '?':
                    table[i][j] = table[i-1][j-1]

                # cur_pattern == '*'
                else:
                    table[i][j] = table[i-1][j-1] | table[i-1][j] | table[i][j-1]

        return table[len_s][len_p]








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
            ]

    for given_str, pattern in examples:
        print(s.isMatch(given_str, pattern))
