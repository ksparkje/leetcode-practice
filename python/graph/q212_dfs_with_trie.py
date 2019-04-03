# 212. Word Search II
# Hard
#
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be used
# more than once in a word.
#
# Example:
#
# Input:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# Output: ["eat","oath"]
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word):
        node = self.head
        for c in word:
            node = node.children[c]
        node.end = True

    def search(self, word):
        node = self.head
        for c in word:
            node = node.children.get(c, None)
            if not node:
                return False
        return node.end


'''
Different when we do DFS. Must check the validity after 
visiting the next point...
Look at (*)
'''
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        i_len = len(board)
        j_len = len(board[0])

        so_far = []

        def search_board(i, j, cur_node, path):
            if cur_node.end:
                so_far.append(path)
                cur_node.end = False

            # This is a special case...
            # We must do this here in order to ensure that
            # so_far appends when cur_node.end
            # (*)
            if not (0 <= i < i_len and 0 <= j < j_len):
                return

            char_on_board = board[i][j]

            if char_on_board not in cur_node.children:
                return

            else:
                path = path + char_on_board
                cur_node = cur_node.children[char_on_board]
                board[i][j] = '#'
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    search_board(i+di, j+dj, cur_node, path)
                board[i][j] = char_on_board

        node = trie.head
        for i in range(i_len):
            for j in range(j_len):
                search_board(i, j, node, '')

        return so_far


if __name__ == '__main__':
    s = Solution()
    input = ([["a"]],    ["a"])
    print(s.findWords(*input))
