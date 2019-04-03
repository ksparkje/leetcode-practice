# 670. Maximum Swap
#
# Given a non-negative integer, you could swap two digits at most once to get the maximum
# valued number. Return the maximum valued number you could get.
#
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
import functools


'''
There are two parts. First, I need to find the max number of whole thing,
so I keep a decreasing stack. Second, I need to know if there were a lower number
before the current element, so keep a minimum so far as another tracker.

Keep a decreasing stack, But don't keep the two same number. Keep the one coming later.

1099867 => 987
min     => 000
           TTT

Also, while creating a stack, Keep a minimum seen so far so that I know
whether the current number has a number before it that's lower than itself.

99867 => 987
min   => 986
         FFT

If minimum is seen before a current elem, the max such elem from that point
is the one I need to swap?

98368 => 98
min   => FT
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        given = [item for item in str(num)]
        min_so_far = '9'
        decreasing = []

        for idx, item in enumerate(given):
            min_so_far = min(min_so_far, item)
            while decreasing and decreasing[-1][-1] <= item:
                decreasing.pop()
            decreasing.append([idx, min_so_far < item, item])

        if all([not has_lower for _, has_lower, _ in decreasing]):
            return num

        for idx, has_lower_elem, item in decreasing:
            if has_lower_elem:
                for lower_idx, lower_item in enumerate(given[:idx]):
                    if lower_item < item:
                        given[idx], given[lower_idx] = given[lower_idx], given[idx]
                        return int(''.join(given))


if __name__ == '__main__':
    s = Solution()
    print(s.maximumSwap(1090901))
    print(s.maximumSwap(98368))
    print(s.maximumSwap(92368))
    print(s.maximumSwap(9765))







