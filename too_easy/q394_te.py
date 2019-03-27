# 394. Decode String

# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside
# the square brackets is being repeated exactly k times. Note that k is
# guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits
# and that digits are only for those repeat numbers, k. For example, there won't
# be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


'''
Lets use stack
If I see numbers, add those numbers.
If I see [, keep the current string and current number in a stack.
    Start over with a new string.
Once ], go down the stack
'''
class Solution:
    # This is a slow implementation...
    # Should really keep chars in a list and connect them in the end...
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string = ''
        cur_number = 0

        for char in s:
            if char.isnumeric():
                cur_number = cur_number * 10 + int(char)

            elif char == '[':
                stack.append(cur_string)
                cur_string = ''
                stack.append(cur_number)
                cur_number = 0

            elif char == ']':
                last_number = stack.pop()
                last_string = stack.pop()
                cur_string = last_string + last_number * cur_string

            else:
                cur_string += char

        return cur_string


if __name__ == '__main__':
    s = Solution()
    input_string = "aab3[a]2[bc]"
    input_string = "2[a2[bc]]3[cd]ef"
    input_string = "3[a2[c]]"
    print(s.decodeString(input_string))

