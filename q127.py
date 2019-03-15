# 127. Word Ladder
# Medium
#
# Given two words (beginWord and endWord), and a dictionary's word list,
# find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
import string


'''
Do BFS
Don't do any(...), instead come up with a set
'''
class Solution_2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        queue = [(beginWord, 1)]

        not_visited = {word for word in wordList}

        if beginWord in not_visited:
            not_visited.remove(beginWord)

        while queue:
            cur_word, distance = queue.pop(0)

            if cur_word == endWord:
                return distance

            word_to_be_del = []
            for word in not_visited:

                # Delete one char per place and see if they are the same.
                if any((cur_word[:i] + cur_word[i+1:]) == (word[:i] + word[i+1:])
                        for i in range(len(cur_word))):
                    # This is a slow process. One could just come up with a new word
                    # and see if that word is in the not_visited...
                    #
                    # i.e. cur_word[:i] + new_char + cur_word[i+1:] for i in range(len(cur_word))
                    #                                               for new char in str.lower_case
                    queue.append((word, distance+1))
                    word_to_be_del.append(word)

            for word in word_to_be_del:
                not_visited.remove(word)

        return 0


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = [(beginWord, 1)]

        not_visited = {word for word in wordList}

        if beginWord in not_visited:
            not_visited.remove(beginWord)

        while queue:
            cur_word, distance = queue.pop(0)

            if cur_word == endWord:
                return distance

            one_char_changed_set = set(cur_word[:i] + ch + cur_word[i+1:]
                                       for i in range(len(cur_word))
                                       for ch in string.ascii_lowercase)

            next_words = not_visited & one_char_changed_set
            not_visited -= next_words
            for word in next_words:
                queue.append((word, distance+1))

        return 0



if __name__ == '__main__':
    s = Solution()
    # print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
    # print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]))

    print(s.ladderLength("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]))














