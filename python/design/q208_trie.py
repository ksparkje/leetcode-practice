# 208. Implement Trie (Prefix Tree)
# Medium
#
# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

import collections
from functools import reduce

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = collections.defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        assert word.isalpha()

        cur_node = self.head
        for char in word:
            # THIS PART IS SUPER INTERESTING!!!
            cur_node = cur_node.children[char]
        cur_node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        assert word.isalpha()

        cur_node = self.head
        for char in word:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
        return cur_node.end


    def startsWith(self, prefix: str) -> bool:
        assert prefix.isalpha()

        cur_node = self.head
        for char in word:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
        return True


class Trie(object):

    def __init__(self):
        T = lambda: collections.defaultdict(T)
        self.root = T()

    def insert(self, word):
        reduce(dict.__getitem__, word, self.root)['#'] = True

    def search(self, word):
        return '#' in reduce(lambda cur, c: cur.get(c, {}), word, self.root)

    def startsWith(self, prefix):
        return bool(reduce(lambda cur, c: cur.get(c, {}), prefix, self.root))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)