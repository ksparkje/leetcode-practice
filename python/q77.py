# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


'''
---------------------    starting_index
[1, 2, 3, 4] choose 2    0
1 + [2, 3, 4] choose 1   1
2 + [3, 4]    choose 1   2
3 + [4]       choose 1   3
---------------------
[1, 2, 3, 4]  choose 3   0
1 + [2, 3, 4] choose 2   1
2 + [3, 4]    choose 2   2
3 + [4]       choose 2
'''
class Solution:
    def combine(self, n: int, k: int):
        '''
        :param n:
        :param k:
        :return: list of lists
        '''

        if k == 0:
            return [[]]

        list_to_choose_from = list(range(1, n+1))

        def choose_l_given_starting_index(l, starting_index):
            if l == 0:
                yield
                return
            # there is less elem to choose from than to choose
            # if n - starting_index < l:
            #     yield
            #     return

            # how many we can choose from == l?
            if n - starting_index == l:
                yield list_to_choose_from[starting_index:]

            else:
                # n - l is the last elem we are choosing from, for this first element of choice
                for idx, item in enumerate(list_to_choose_from[starting_index: n - l + 1],
                                           starting_index):
                    for remaining in choose_l_given_starting_index(l-1, idx+1):
                        if remaining:
                            yield [item] + remaining
                        else:
                            yield [item]

        return [item for item in choose_l_given_starting_index(k, 0)]


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4,3))
    print(s.combine(2,1))
    print(s.combine(1,0))

