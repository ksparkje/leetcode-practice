from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cache = {}
        cells = tuple(cells)
        re = [cells]
        for i in range(N):
            if cells in cache:
                # find where periodic sequence begin
                b = cache[cells]
                # find the period
                t = i - b
                return re[b + (N - b) % t]
            new_cell = self.shift(cells)
            re.append(new_cell)
            cache[cells] = i
            cells = new_cell
        return cells

    @staticmethod
    def shift(base):
        new_cell = []
        new_cell.append(0)
        for i in range(1, len(base) - 1):
            new_cell.append(base[i - 1] ^ base[i + 1] ^ 1)
        new_cell.append(0)
        return tuple(new_cell)


if __name__ == '__main__':
    s = Solution()
    input = ([0,1,0,1,1,0,0,1], 15)
    print(s.prisonAfterNDays(*input))