# Input: [
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation:
# At the beginning, you start at square 1 [at row 5, column 0].
# You decide to move to square 2, and must take the ladder to square 15.
# You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
# You then decide to move to square 14, and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.


class Solution:
    def snakesAndLadders(self, board) -> int:
        '''
        :param board:
        :return:
        '''

        len_board = len(board)

        def get_row_col_given(s):
            quot, rem = divmod(s-1, len_board)
            row = len_board - 1 - quot
            col = len_board - 1 - rem if quot % 2 else rem
            return row, col

        so_far = {1: 0}

        queue = [1]

        while queue:
            cur_node = queue.pop(0)

            if cur_node == len_board ** 2:
                return so_far[cur_node]

            for next_node in range(cur_node+1, min(len_board ** 2, cur_node + 6) + 1):
                r, c = get_row_col_given(next_node)

                # Check if I am directed by ladder
                if board[r][c] != -1:
                    next_node = board[r][c]

                if next_node not in so_far:
                    so_far[next_node] = so_far[cur_node] + 1
                    queue.append(next_node)

        return -1
