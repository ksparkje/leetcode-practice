# Find the longest substring with k unique characters in a given string
# Given a string you need to print longest possible substring that has exactly M
# unique characters. If there are more than one substring of longest possible length,
# then print any one of them.

# Examples:
#
# "aabbcc", k = 1
# Max substring can be any one from {"aa" , "bb" , "cc"}.
#
# "aabbcc", k = 2
# Max substring can be any one from {"aabb" , "bbcc"}.
#
# "aabbcc", k = 3
# There are substrings with exactly 3 unique characters
# {"aabbcc" , "abbcc" , "aabbc" , "abbc" }
# Max is "aabbcc" with length 6.
#
# "aaabbb", k = 3
# There are only two unique characters, thus show error message.

# Leetcode 340, also found on
# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/


'''
Have a start pointer, then iterate through...
k = 2
-
aabbcc
|

-
aabbcc
 |

-
aabbcc
  |

-
aabbcc
   |

  -
aabbcc
    |
'''
import collections

'''
Keep a counter, and left_idx
longest_so_far = ''
for right_index, every character
    while counter has more than k unique elem,
        if right_index - left_index + 1 >= max_dist_so_far:
            max_dist_so_far = right - left_index + 1
            longest_so_far = given_str[left_index: right_index+1]
        left_index += 1
'''
class Unique:
    def __init__(self):
        self.k = 0
        self.counter = collections.Counter()

    def add(self, item):
        self.counter[item] += 1
        if self.counter[item] == 1:
            self.k += 1

    def remove(self, item):
        self.counter[item] -= 1
        if self.counter[item] == 0:
            self.k -= 1


class Solution2:
    def find_longest_substring_with_k_unique_char(self, given_str, k):
        unique_counter = Unique()
        left_idx = 0
        longest_so_far = ''
        for right_idx, char in enumerate(given_str):
            unique_counter.add(char)

            while unique_counter.k > k:
                unique_counter.remove(given_str[left_idx])
                left_idx += 1

            if len(longest_so_far) < right_idx - left_idx + 1:
                longest_so_far = given_str[left_idx: right_idx+1]

        return longest_so_far


class Solution:
    def find_longest_substring_with_k_unique_char(self, given_str, k):
        start_idx = 0
        cur_max = 0
        character_count = {}
        max_dictionary = collections.defaultdict(list)

        for idx, c in enumerate(given_str):
            if c in character_count:
                character_count[c] += 1
            else:
                while len(character_count) == k:
                    current_count = character_count[given_str[start_idx]]
                    if current_count == 1:
                        character_count.pop(given_str[start_idx])
                    else:
                        character_count[given_str[start_idx]] -= 1
                    start_idx += 1

                character_count[c] = 1

            this_length = idx - start_idx + 1
            # record the max
            cur_max = max(cur_max, this_length)

            max_dictionary[this_length].append(given_str[start_idx: idx + 1])

        return max_dictionary


if __name__ == '__main__':
    s = Solution2()
    print(s.find_longest_substring_with_k_unique_char('aabbcc', 2))
    print(s.find_longest_substring_with_k_unique_char("aaabbb", 3))
    print(s.find_longest_substring_with_k_unique_char("abcdaaabbfff", 3))
    print(s.find_longest_substring_with_k_unique_char("facdabbb", 2))
    print(s.find_longest_substring_with_k_unique_char("aabacbebebe", 3))


































