# 140. Word Break II
# Hard
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []


from typing import List
from functools import reduce
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        if not s:
            return []

        if not wordDict:
            return []

        max_len_in_dict = reduce(lambda x, y: max(x, len(y)), wordDict, 0)
        my_dict = {item for item in wordDict}
        visited = defaultdict(list)

        def dfs(given_s, path: List[str]):
            # Return me a possible path
            if not given_s:
                return path

            if given_s in visited:
                return visited[given_s]

            all_rest = []
            current_partial = []
            for idx, c in enumerate(given_s):
                if idx < max_len_in_dict:
                    current_partial += [c]
                    this_word = ''.join(current_partial)
                    if this_word in my_dict:
                        rest = given_s[idx+1:]
                        rest_list = dfs(rest, [this_word])
                        visited[rest].append(' '.join(rest_list))
                        all_rest += rest_list

                else:
                    break

            visited[given_s].extend(' '.join(path) + ' ' + item
                                    for rest in all_rest
                                    for item in visited[rest])
            print(visited[given_s])
            return visited[given_s]

        temp = dfs(s, [])
        return temp


if __name__ == '__main__':

    s = Solution()
    input = ("catsanddog",     ["cat", "cats", "and", "sand", "dog"])
    # input = ('leetcode', ["leet", "code"])

    print(s.wordBreak(*input))
