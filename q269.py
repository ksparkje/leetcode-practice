# 269. Alien Dictionary
#
# There is a new alien language which uses the latin alphabet. However, the order
# among letters are unknown to you. You receive a list of non-empty words from the
# dictionary, where words are sorted lexicographically by the rules of this new language.
# Derive the order of letters in this language.
#
# Example 1:
#
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#
# Output: "wertf"
# Example 2:
#
# Input:
# [
#   "z",
#   "x"
# ]
#
# Output: "zx"
# Example 3:
#
# Input:
# [
#   "z",
#   "x",
#   "z"
# ]
#
# Output: ""
#
# Explanation: The order is invalid, so return "".
from collections import defaultdict


'''
Build graph according to the list of strings

First character different: source -> target

알고리즘 문제해결 전략 에서도 소개된 바가 있음...
'''
class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # build graph
        here_to_there = defaultdict(list)
        for word in zip(words, words[1:]):
            for c1, c2 in zip(*word):
                if c1 != c2:
                    here_to_there[c1].append(c2)
                    break

        all_char = set(''.join(words))
        visiting = set()
        visited = set()

        result = []

        # toposort...
        def dfs(cur_char):
            if cur_char in visiting:
                return False
            if cur_char in visited:
                return True

            visiting.add(cur_char)
            # Note: Things do get a lot faster with .get function instead...
            # But the code gets messier, so ignoring
            for there in here_to_there[cur_char]:
                if not dfs(there):
                    return False
            visiting.remove(cur_char)
            visited.add(cur_char)
            result.append(cur_char)
            return True

        if not all(dfs(char) for char in all_char):
            return ''

        return ''.join(result[::-1])
