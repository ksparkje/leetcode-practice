# 76. Minimum Window Substring

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"


from collections import Counter


'''
Gameplan:
Keep a dictionary of {needed_chars: counts}, `missing: int` as total number of missing chars.
Make a sliding window, by moving right, such that from s[left:right] covers all of the elem in t.
Then, start moving left until we are missing a character
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing_counts = len(t)
        character_counter = Counter(t)
        last_seen_idx = {}

        if not all(key in s for key in character_counter) or len(s) < len(t):
            return ''

        starting_idx = 0
        min_pair = []

        for idx, char in enumerate(s):
            if char in character_counter:
                # decrease only if character counts are greater than 0
                missing_counts -= character_counter[char] > 0
                character_counter[char] -= 1
                last_seen_idx[char] = idx

                # it's possible to have bbbab (repeating characters)
                while missing_counts == 0:

                    if not min_pair:
                        min_pair = [starting_idx, idx]
                    else:
                        min_pair = ([starting_idx, idx]
                                    if idx - starting_idx < min_pair[1] - min_pair[0]
                                    else min_pair)

                    starting_char = s[starting_idx]
                    if starting_char in character_counter:
                        if character_counter[starting_char] == 0:
                            missing_counts += 1
                        character_counter[starting_char] += 1
                    starting_idx += 1

        return s[min_pair[0]: min_pair[1]+1] if min_pair else ''


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow('babb', 'baba'))
