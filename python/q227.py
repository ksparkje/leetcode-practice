# 227. Basic Calculator II

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: "3+2*2"
# Output: 7
# Example 2:
#
# Input: " 3/2 "
# Output: 1
# Example 3:
#
# Input: " 3+5 / 2 "
# Output: 5


class Solution:
    def calculate(self, s: str) -> int:

        temp_val = 0
        kept = []
        prev_operator = '+'

        for idx, item in enumerate(s):

            # item could be numeric or operator
            if item.isnumeric():
                temp_val = temp_val*10 + int(item)

            # There is never a case it's both numeric and operator...
            # idx == len(s) - 1 is for the last elem case, in which point
            # the item will be numeric, but it's okay since it's the last step
            if item in ('+', '-', '/', '*') or idx == len(s) - 1:
                if prev_operator == '+':
                    kept += [temp_val]
                elif prev_operator == '-':
                    kept += [-temp_val]
                elif prev_operator == '*':
                    new_val = kept.pop() * temp_val
                    kept += [new_val]
                else: # previous operator was /
                    new_val = int(kept.pop() / temp_val)
                    kept += [new_val]

                # update operator
                prev_operator = item
                temp_val = 0

        return sum(kept)


'''
Tough part is how to deal with the last elem!
1. Must be kept until we find another operator.
2. Keep two if! not elif!
'''
class Solution_2:
    def calculate(self, s: str) -> int:
        '''
        :param s:
        :return:
        '''
        prev_operator = '+'
        cur_number = 0
        kept = []

        for idx, char in enumerate(s):
            if char.isnumeric():
                cur_number = cur_number * 10 + int(char)
            # This must be if!!!!!!!
            if char in ('*', '/',  '+', '-') or (idx == len(s) - 1):
                print(char)
                if prev_operator == '+':
                    kept.append(cur_number)
                elif prev_operator == '-':
                    kept.append(-cur_number)
                elif prev_operator == '*':
                    kept.append(kept.pop() * cur_number)
                # char == '/
                else:
                    temp = int(kept.pop() / cur_number)
                    kept.append(temp)
                prev_operator = char
                cur_number = 0

        return sum(kept)


if __name__ == '__main__':
    s = Solution_2()

    print(s.calculate("14-3/2"))

