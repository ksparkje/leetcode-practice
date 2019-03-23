# 301. Remove Invalid Parentheses
#
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Example 1:
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:
#
# Input: ")("
# Output: [""]
'''
Ignoring my Previous solutions...
Because, this solution is too good to pass up...
    http://bookshadow.com/weblog/2015/11/05/leetcode-remove-invalid-parentheses/

근래 본것중 원탑은 몰라도 최강 중 하나...
'''
import collections


class SolutionDiscussed:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def mismatch_count(s_given):
            a = b = 0
            # Looks super confusing at first, but this is
            # because cases like ))(( => return 4
            for c in s_given:
                a += {'(': 1,
                      ')': -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        def dfs(s_given):
            count = mismatch_count(s_given)
            if count == 0:
                return [s_given]
            ans = []
            for idx, c in enumerate(s_given):
                if c in ('(', ')'):
                    without = s_given[:idx] + s_given[idx + 1:]
                    if without not in visited and mismatch_count(without) < count:
                        visited.add(without)
                        # This part is NICE
                        ans.extend(dfs(without))
            return ans

        visited = set([s])
        return dfs(s)

    def bfsRemoveInvalidParentheses(self, s: str) -> List[str]:

        def valid(given_str):
            a = 0
            for c in given_str:
                a += {'(': 1,
                      ')': -1}.get(c, 0)
                if a < 0:
                    return False
            return a == 0

        def bfs(given_str):
            # queue = collections.deque([given_str])
            queue = [given_str]
            visited = set([given_str])
            ans = []
            done = False
            while queue:
                cur_string = queue.pop(0)
                if valid(cur_string):
                    done = True
                    ans.append(cur_string)
                if done:
                    continue
                for idx, c in enumerate(cur_string):
                    if c in ('(', ')'):
                        without = cur_string[:idx] + cur_string[idx+1:]
                        if without not in visited:
                            visited.add(without)
                            queue.append(without)
            return ans
        result = bfs(s)
        return result if result else ['']

    def bfsPruneRemoveInvalidParentheses(self, s: str) -> List[str]:

        def num_mismatch(given_str):
            a = b = 0
            for c in given_str:
                a += {'(': 1,
                      ')': -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        def bfs(given_str):
            # queue = collections.deque([given_str])
            queue = [given_str]
            visited = set([given_str])
            ans = []
            done = False
            while queue:
                cur_string = queue.pop(0)
                current_mis = num_mismatch(cur_string)
                if current_mis == 0:
                    done = True
                    ans.append(cur_string)
                if done:
                    continue
                for idx, c in enumerate(cur_string):
                    if c in ('(', ')'):
                        without = cur_string[:idx] + cur_string[idx+1:]
                        if without not in visited and num_mismatch(without) < current_mis:
                            visited.add(without)
                            queue.append(without)
            return ans

        result = bfs(s)
        return result if result else ['']


'''
My impression/observation

If it's (, the best we can do is just remove (. There is not much we can do.
So the interesting case is missing ). But missing ) in a row doesn't do anything either.
So focus on one missing ).

(    )   (   )    )
+1, -1, +1, -1,  -1
1    0   1   0   -1

())(
In this case () is the only option

()())(
In this case, when paran count == -1
walk right and try removing all closing parans before current index.
The result should be a list of possible combos.
()() (
(()) (


()())())
     |
In this case, i dont think the ones before | would change much.
Therefore, focus only from the starting of |. Keep this result in a separate list...


When there are two in a row. e.g ())), just dump the ones coming after the first.
Now, with all the different elem in each list, combine them?

[ [()(), (())], [()] ] => [()()(), (())()]
'''
from typing import List


class Solution:

    def indecies_removed(self, s, indecies):
        return [s[:index] + s[index+1:] + ')' for index in indecies]

    def find_all_closing(self, s:str) -> List[int]:
        return [idx for idx, char in enumerate(s) if char == ')']

    def set_next_starting(self, s:str, starting_index: int) -> int:
        for idx, char in enumerate(s[starting_index+1:], starting_index + 1):
            if char == '(':
                return idx
        return idx + 1

    def permute(self, parens_to_permute: List[List[str]]) -> List:
        if not parens_to_permute:
            yield []
        else:
            for item in parens_to_permute[0]:
                for rest in self.permute(parens_to_permute[1:]):
                    print([item] + rest)
                    yield [item] + rest


    def removeInvalidParentheses(self, s: str) -> List[str]:

        counter = 0
        next_start_idx = 0

        parenthesis_to_permute = []

        for idx, char in enumerate(s):
            if idx < next_start_idx:
                continue

            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
                if counter < 0:
                    counter = 0

                    current_string_of_interest = s[next_start_idx: idx]
                    parenthesis_to_permute.append([current_string_of_interest])
                    # find all closing index starting from next_start_idx
                    closing_indecies = self.find_all_closing(current_string_of_interest)

                    # return a list with those indecies removed
                    valid_parenthesis = self.indecies_removed(current_string_of_interest, closing_indecies)
                    parenthesis_to_permute.append([valid_parenthesis])

                    # set the next_start_idx such that it's the new starting point of (
                    next_start_idx = self.set_next_starting(s, idx)


        if next_start_idx < idx:
            parenthesis_to_permute.append([s[next_start_idx:]])

        print(parenthesis_to_permute)

        # Permute those items
        return [item for item in self.permute(parenthesis_to_permute)]


if __name__ == '__main__':
    s = Solution()
    test_case = '()())()'
    test_case = "(a)())()"
    print(s.removeInvalidParentheses(test_case))





