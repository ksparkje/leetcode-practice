# 224. Basic Calculator

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .
#
# Example 1:
#
# Input: "1 + 1"
# Output: 2
# Example 2:
#
# Input: " 2-1 + 2 "
# Output: 3


class Solution:
    def calculate(self, s: str) -> int:
        prev_operator = '+'
        so_far = [[]]
        temp_number = 0

        s += '+0'

        for idx, item in enumerate(s):
            if item.isnumeric():
                temp_number = temp_number * 10 + int(item)

            elif item != ' ':
                print(so_far)
                if item == '(':
                    so_far[-1].append(prev_operator)
                    so_far += [[]]
                    prev_operator = '+'
                elif item == ')':
                    temp_number = temp_number if prev_operator == '+' else -temp_number
                    last_elem_sum = sum(so_far.pop()) + temp_number
                    if so_far and so_far[-1].__len__():
                        last_operator = so_far[-1][-1]
                        so_far[-1][-1] = last_elem_sum if last_operator == '+' else -last_elem_sum
                    else:
                        so_far[-1].append([last_elem_sum])
                    prev_operator = '+'
                else: # It's either + or -
                    if so_far and so_far[-1].__len__():
                        so_far[-1].append(temp_number if prev_operator == '+' else -temp_number)
                    else:
                        so_far[-1] = [temp_number]
                    prev_operator = item
                temp_number = 0

        return sum(sum(item) for item in so_far)


if __name__ == '__main__':
    s = Solution()
    print(s.calculate('1+(2+3-(5+6) + 2)'))

