# 139. Word Break
# Medium
#
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty
# words, determine if s can be segmented into a space-separated sequence of one or more
# dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false


'''
Start with the first character in a given string, expand each char.
While each char's length is less than max len of wordDict, try it, and check if
the rest can be made. When you check it, build the cache?
'''
from typing import List
from functools import reduce


class Solution:
    def wordBreakTable(self, s: str, wordDict: List[str]) -> bool:
        s = '_' + s
        max_len_in_dict = reduce(lambda x, y: max(x, len(y)), wordDict, 0)
        my_dict = {item for item in wordDict}

        table = [False] * len(s)
        table[0] = True
        for i in range(1, len(s)):
            for j in range(1, min(max_len_in_dict, len(s) - i)):
                table[i] = table[j-i] and s[i: i+j] in my_dict
        print(table)
        return table[-1]






    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if not s:
            return True

        if not wordDict:
            return False

        max_len_in_dict = reduce(lambda x, y: max(x, len(y)), wordDict, 0)
        my_dict = {item for item in wordDict}
        so_far = {}

        def dfs(given_s):
            if not given_s:
                return True

            if given_s in so_far:
                return so_far[given_s]

            possible = False
            current_partial = []
            for idx, c in enumerate(given_s):
                if idx < max_len_in_dict:
                    current_partial += [c]
                    this_word = ''.join(current_partial)
                    if this_word in my_dict:
                        possible |= dfs(given_s[idx+1:])
                else:
                    break

            so_far[given_s] = possible
            return possible

        return dfs(s)


if __name__ == '__main__':

    s = Solution()
    input = ('leetcode', ["leet", "code"])

    print(s.wordBreakTable(*input))



















