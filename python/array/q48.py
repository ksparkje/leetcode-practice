# 48. Rotate Image
# Medium
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix
# directly. DO NOT allocate another 2D matrix and do the rotation.

'''
[[1, 2, 3]            [7, 4, 1]
 [4, 5, 6]    ->      [8, 5, 2]
 [7, 8, 9]]           [9, 6, 3]

swap (1, 3), then (3, 9), then (9, 7)...
Let's name (i,j) = (0,0), swapping index (si, sj). Notice if I just do the top row,
it's done for the all outside rows.

matrixbove is the old way...
matrix Better way:
divide into four parts via
a b | e f  such that the quadrant 1 is the only place we start from...
c d | g h
----------
i j | k l
m n | o p
Don't focus on 'a'. Start with 'b'.


Also Note:
    1   2    3  | 4   5
    6   7    8  | 9   10
    -----------
    11  12 | 13 | 14  15
            -----------
    16  17 | 18  19  20
    21  22 | 23  24  25
'''


class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix) // 2):
            for j in range(len(matrix) - (len(matrix) // 2)):
                matrix[j][~i], matrix[~i][~j], matrix[~j][i], matrix[i][j] = (
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i])

        return matrix


class Solution2(object):
    def rotate(self, matrix):
        for i in range(len(matrix)//2):
            #              여기가 무조건 ................
            for j in range(len(matrix) - len(matrix)//2):
                #             Notice this swap in x and y
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                    matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]


if __name__ == '__main__':
    input = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    s.rotate(input)
    print(input)