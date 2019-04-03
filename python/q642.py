# 642. Design Search Autocomplete System
# Hard
#
# Design a search autocomplete system for a search engine. Users may input a sentence
# (at least one word and end with a special character '#'). For each character they type
# except '#', you need to return the top 3 historical hot sentences that have prefix the
# same as the part of sentence already typed. Here are the specific rules:
#
# The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
# The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one).
# If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
# If less than 3 hot sentences exist, then just return as many as you can.
# When the input is a special character, it means the sentence ends, and in this case, you need to
# return an empty list.

# Your job is to implement the following functions:
#
# The constructor function:
#
# AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical
# data. Sentences is a string array consists of previously typed sentences. Times is the corresponding
# times a sentence has been typed. Your system should record these historical data.
#
# Now, the user wants to input a new sentence. The following function will provide the next character
# the user types:
#
# List<String> input(char c): The input c is the next character typed by the user. The character will
# only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the
# previously typed sentence should be recorded in your system. The output will be the top 3 historical
# hot sentences that have prefix the same as the part of sentence already typed.


'''
Initial Thoughts:
    Sentences need to be kept sorted by the order of times, tie-break on ascii value.
    When input is given, keep the inputs together until the `#`.

'''
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0


class AutocompleteSystem(object):
   def __init__(self, sentences, times):
       self.root = TrieNode()
       self.keyword = ""
       for i, sentence in enumerate(sentences):
           self.addRecord(sentence, times[i])

   def addRecord(self, sentence, hot):
       p = self.root
       for c in sentence:
           if c not in p.children:
               p.children[c] = TrieNode()
           p = p.children[c]
       p.isEnd = True
       p.data = sentence
       p.rank -= hot

   def dfs(self, root):
       ret = []
       if root:
           if root.isEnd:
               ret.append((root.rank, root.data))
           for child in root.children:
               ret.extend(self.dfs(root.children[child]))
       return ret

   def search(self, sentence):
       p = self.root
       for c in sentence:
           if c not in p.children:
               return []
           p = p.children[c]
       return self.dfs(p)

   def input(self, c):
       results = []
       if c != "#":
           self.keyword += c
           results = self.search(self.keyword)
       else:
           self.addRecord(self.keyword, 1)
           self.keyword = ""
       return [item[1] for item in sorted(results)[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
