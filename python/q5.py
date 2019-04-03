# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def f(i, j):
            '''
            :param i: starting_index
            :param j: ending_index
            :return: value if possible else -1
            '''
            if i - j > 0:
                return (0, (i, j))
            if i == j:
                return (1, (i, j))

            i_j = (i, j)
            if i_j in table:
                return table[i_j]

            if s[i] == s[j]:
                value = f(i+1, j-1)
                if value[0] != -1:
                    value = (value[0] + 2, (i, j))
            else:
                value = (-1, (-1, -1))

            table[i_j] = value
            return value

        table = {}
        max_val = 0
        indecies = (-1, -1)
        for idx in range(s.__len__()):
            for j in range(idx, s.__len__()):
                cur_dist, cur_indecies = f(idx, j)
                if cur_dist > max_val:
                    max_val = cur_dist
                    indecies = cur_indecies

        return s[indecies[0]: indecies[1]+1]


def compute_longest_palindromic_substring(given_string):
    len_string = len(given_string)

    table = [[False]*len_string for _ in range(len_string)]

    max_len, i_j = 0, [-1, -1]

    for i in range(len_string):
        table[i][i] = True
        i_j = [i, i]

    for i in range(len_string-1):
        if given_string[i] == given_string[i+1]:
            table[i][i+1] = True
            max_len = 2
            i_j = [i, i+1]

    for j in range(2, len_string):
        for i in range(0, j-1):
            if given_string[i] == given_string[j] and table[i+1][j-1]:
                table[i][j] = True
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    i_j = [i, j]

    return given_string[i_j[0]:i_j[1]+1]


if __name__ == '__main__':
    s = Solution()
    test_string = 'aaaaaaaaaaabcdefggggggggggggggggggggggggggggggfedcbaaaaaaaaaaa'
    print(s.longestPalindrome(test_string))
    print(len(test_string))

    print(compute_longest_palindromic_substring(test_string))


