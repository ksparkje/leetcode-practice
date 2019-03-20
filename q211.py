# 211. Add and Search Word - Data structure design
# Medium
#
# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.end = False
        self.dict = defaultdict(TrieNode)


class WordDictionary:

    def __init__(self):
        self.head_dict = TrieNode()

    def addWord(self, word: str) -> None:
        dict_ptr = self.head_dict
        for char in word:
            dict_ptr = dict_ptr.dict[char]
        dict_ptr.end = True

    def search(self, word: str) -> bool:
        """
        A word could contain the dot character '.' to represent any one letter.
        """
        def search_from_dict_ptr(dict_ptr, word_remaining):
            # return True if dict_ptr can finish with word_remaining

            if not word_remaining:
                return dict_ptr.end

            first_char = word_remaining[0]

            if first_char == '.':
                return any(search_from_dict_ptr(dict_ptr.dict.get(c), word_remaining[1:])
                           for c in dict_ptr.dict)
            elif first_char in dict_ptr.dict:
                return search_from_dict_ptr(dict_ptr.dict.get(first_char), word_remaining[1:])
            else:
                return False

        return search_from_dict_ptr(self.head_dict, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)