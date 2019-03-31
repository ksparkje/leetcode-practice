# 472. Concatenated Words
# Hard
#
# Given a list of words (without duplicates), please write a program that returns all concatenated
# words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter
# words in the given array.
#
# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Note:
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.


'''
Initial thoughts. Sort the words by length of each word.

Build Trie: First, check if the word you're checking is in the trie.
Then have a counter that counts such segments. If it can be split into more than two with
ending properly, put that into the returning list. Add the new word.
'''
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        word_dict = set(words)
        visited = {}

        def dfs(word):
            if word in visited:
                return visited[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if ((prefix in word_dict or dfs(prefix)) and
                    (suffix in word_dict or dfs(suffix))):
                    visited[word] = True
                    return True

            visited[word] = False
            return False

        words.sort(key=len)
        return [word for word in words if dfs(word)]


if __name__ == '__main__':

    input = ["rfkqyuqfjkx","","vnrtysfrzrmzl","gfve","qfpd","lqdqrrcrwdnxeuo","q",
             "klaitgdphcspij","hbsfyfv","adzpbfudkklrw","aozmixr","ife","feclhbvfuk",
             "yeqfqojwtw","sileeztxwjl","ngbqqmbxqcqp","khhqr","dwfcayssyoqc","omwufbdfxu",
             "zhift","kczvhsybloet","crfhpxprbsshsjxd","ilebxwbcto","yaxzfbjbkrxi","imqpzwmshlpj",
             "ta","hbuxhwadlpto","eziwkmg","ovqzgdixrpddzp","c","wnqwqecyjyib","jy","mjfqwltvzk",
             "tpvo","phckcyufdqml","lim","lfz","tgygdt","nhcvpf","fbrpzlk","shwywshtdgmb","bkkxcvg",
             "monmwvytby","nuqhmfj","qtg","cwkuzyamnerp","fmwevhwlezo","ye","hbrcewjxvcezi","tiq",
             "tfsrptug","iznorvonzjfea","gama","apwlmbzit","s","hzkosvn","nberblt","kggdgpljfisylt",
             "mf","h","bljvkypcflsaqe","cijcyrgmqirz","iaxakholawoydvch","e","gttxwpuk","jf",
             "xbrtspfttota","sngqvoijxuv","bztvaal","zxbshnrvbykjql","zz","mlvyoshiktodnsjj","qplci",
             "lzqrxl","qxru","ygjtyzleizme","inx","lwhhjwsl","endjvxjyghrveu","phknqtsdtwxcktmw","wsdthzmlmbhjkm",
             "u","pbqurqfxgqlojmws","mowsjvpvhznbsi","hdkbdxqg","ge","pzchrgef","ukmcowoe","nwhpiid",
             "xdnnl","n","yjyssbsoc","cdzcuunkrf","uvouaghhcyvmlk","aajpfpyljt","jpyntsefxi","wjute",
             "y","pbcnmhf","qmmidmvkn","xmywegmtuno","vuzygv","uxtrdsdfzfssmel","odjgdgzfmrazvnd","a",
             "rdkugsbdpawxi","ivd","bbqeonycaegxfj","lrfkraoheucsvpi","eqrswgkaaaohxx","hqjtkqaqh",]

    s = Solution()
    print(s.findAllConcatenatedWordsInADict(input))


