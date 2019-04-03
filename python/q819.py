# 819. Most Common Word
# Easy
#
# Given a paragraph and a list of banned words, return the most frequent
# word that is not in the list of banned words.  It is guaranteed there
# is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of
# punctuation.  Words in the paragraph are not case sensitive.  The answer
# is in lowercase.
import string

from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        all_word = []
        cur_word = []
        for char in paragraph:
            if char in string.ascii_letters:
                cur_word += [char.lower()]
            elif cur_word:
                all_word.append(''.join(cur_word))
                cur_word = []
        # 이런 경우가 꽤 생각보다 많은 듯...
        if cur_word:
            all_word.append(''.join(cur_word))

        counted_words = Counter(all_word)

        for key in banned:
            if key in counted_words:
                counted_words.pop(key)

        return counted_words.most_common(1)[0][0] if counted_words else ''





if __name__ == '__main__':
    s = Solution()
    input = ("Bob", [])
    print(s.mostCommonWord(*input))
