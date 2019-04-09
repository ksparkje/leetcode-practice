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
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []
        myDict = set(wordDict)
        # max_length = max(map(lambda x: len(x), myDict))
        length = len(s)
        cache = defaultdict(list)

        def dfs(start_idx, whole_string) -> List[str]:
            if start_idx == length:
                return []

            if start_idx in cache:
                return cache[start_idx]

            cur_result = []
            for idx in range(start_idx+1, length+1):
                # if (idx - start_idx) > max_length:
                #     break
                this_word = s[start_idx: idx]
                if this_word in myDict:
                    if idx == length:
                        _ = dfs(idx, whole_string + this_word)
                        cur_result += [this_word]
                    else:
                        rest = dfs(idx, whole_string + this_word)
                        cur_result += [this_word + ' ' + item for item in rest]

            cache[start_idx].extend(cur_result)
            return cur_result

        return dfs(0, '')


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        if not s:
            return []

        if not wordDict:
            return []

        my_dict = {item for item in wordDict}
        visited = defaultdict(list)

        def dfs(given_s):
            # Return me a possible path
            if not given_s:
                return []

            if given_s in visited:
                return visited[given_s]

            ret = []
            for word in my_dict:
                if given_s.startswith(word):

                    # THIS MUST BE HERE
                    if len(word) == len(given_s):
                        ret.append(word)
                        # This ensures the correct implementation even when
                        # rest_list is returned [] and therefore no for-loop
                        # happens in line  (*)

                    else:
                        rest_list = dfs(given_s[len(word):])
                        for item in rest_list:  # (*)
                            ret += [word + ' ' + item]

            visited[given_s].extend(ret)
            return visited[given_s]

        return dfs(s)


if __name__ == '__main__':

    s = Solution()
    input = ("catsanddog",     ["cat", "cats", "and", "sand", "dog"])

    print(s.wordBreak(*input))
