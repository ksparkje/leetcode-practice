# 336. Palindrome Pairs
# Hard
#
# Given a list of unique words, find all pairs of distinct indices (i, j) in the
# given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
#
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example 2:
#
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
from typing import List


'''
Naturally I ask, "what must be added to make an elem a palindrome?

"abcd" -> some_palindrome + "dcba", or "cba"
"catt" -> some_palindrome + "ttac", or "tac", "ac"
"cattt" -> some_palindrome + "tttac", or "ttac", "tac", "ac"

Instead of thinking about it rather complicatedly, try something sorta bruteforce...
"abcd" -> prefix [a, ab, abc, abcd], postfix [bcd, cd, d]

for idx, word in enumerate(words):
    If prefix[::-1] exists in `words` and postfix is palindrome, we've found a pair
        [idx, dict[prefix[::-1]]
    If postfix[::-1] exists in `words`, and prefix is palindrome, we've found a pair
        [dict[postfix[::-1], idx]

'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        all_words = {word: idx for idx, word in enumerate(words)}

        so_far = []
        for idx, word in enumerate(words):
            for j in range(len(word)+1):
                prefix_reversed, postfix_reversed = word[:j][::-1], word[j:][::-1]
                prefix_pal = prefix_reversed == prefix_reversed[::-1]
                postfix_pal = postfix_reversed == postfix_reversed[::-1]

                if postfix_pal and prefix_reversed in all_words and all_words[prefix_reversed] != idx:
                    so_far.append([idx, all_words[prefix_reversed]])

                if j and prefix_pal and postfix_reversed in all_words and all_words[postfix_reversed] != idx:
                    so_far.append([all_words[postfix_reversed], idx])

        return so_far














































