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
        elem_of_interest = set(t)
        print(elem_of_interest)

        needed = Counter(t)
        missing_counts = len(t)

        left, so_far_left, so_far_right = 0, 0, 1 << 32 - 1

        for right, right_elem in enumerate(s):
            if needed[right_elem] > 0:
                missing_counts -= 1
            if right_elem in elem_of_interest:
                needed[right_elem] -= 1

            while left < right and missing_counts == 0:
                if s[left] in elem_of_interest:
                    print(needed)
                    needed[s[left]] += 1
                    if needed[s[left]] == 0:
                        missing_counts += 1
                        needed[s[left]] += 1
                        # Checking if it's the new best
                        if so_far_right - so_far_left > right - left:
                            so_far_left, so_far_right = left, right
                left += 1

        return s[so_far_left:so_far_right+1]



if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
