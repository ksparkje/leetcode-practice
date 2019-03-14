# 651. 4 Keys Keyboard

# Imagine you have a special keyboard with the following keys:
#
# Key 1: (A): Print one 'A' on screen.
# Key 2: (Ctrl-A): Select the whole screen.
# Key 3: (Ctrl-C): Copy selection to buffer.
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
#
# Now, you can only press the keyboard for N times (with the above four keys),
# find out the maximum numbers of 'A' you can print on screen.


def four_key_strokes(n):
    so_far = {}

    def helper(left_over):
        if left_over in so_far:
            return so_far[left_over]
        else:
            cur_max = 0
            for steps_before_copy_paste in range(left_over - 3, 0, -1):
                # Given left_over == 8,
                # if steps_before_copy_paste = 5
                # 8 - 5 - 1 = 2 is the number of times I can multiply by.
                # if steps_before_copy_paste = 4
                # 8 - 4 - 1 = 3 is the number of times I can multiply by.
                here = (left_over - steps_before_copy_paste - 1) * helper(steps_before_copy_paste)
                cur_max = max(cur_max, here)

            so_far[left_over] = cur_max
            return cur_max

    for idx in range(7):
        so_far[idx] = idx

    helper(n)
    return so_far[n]

class Solution(object):
    @staticmethod
    def maxA(N):
        best = [0, 1, 2, 3, 4, 5, 6, 9, 12,
                16, 20, 27, 36, 48, 64, 81]
        q = (N - 11) // 5 if N > 15 else 0
        return best[N - 5*q] * 4**q


if __name__ == '__main__':

    print(four_key_strokes(8) == Solution.maxA(8))
    print(four_key_strokes(12) == Solution.maxA(12))
    print(four_key_strokes(23) == Solution.maxA(23))
