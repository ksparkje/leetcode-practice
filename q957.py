# 957. Prison Cells After N Days
# Medium
#
# There are 8 prison cells in a row, and each cell is either occupied or vacant.
#
# Each day, whether the cell is occupied or vacant changes according to the following rules:
#
# If a cell has two adjacent neighbors that are both occupied or both vacant, then the
# cell becomes occupied.
# Otherwise, it becomes vacant.
# (Note that because the prison is a row, the first and the last cells in the row can't
# have two adjacent neighbors.)
#
# We describe the current state of the prison in the following way: cells[i] == 1 if the
# i-th cell is occupied, else cells[i] == 0.
#
# Given the initial state of the prison, return the state of the prison after N days (and N
# such changes described above.)
#
# Example 1:
#
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation:
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
#
# Example 2:
#
# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]

from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        def get_next(given_cells):
            return [0] + [(i == j)*1 for i, j in zip(given_cells, given_cells[2:])] + [0]

        items = []
        so_far = set()

        for _ in range(N):
            cur_cell = tuple(cells)
            if cur_cell in so_far:
                # THIS IS THE CRUX OF THIS PROBLEM!!!
                cycle_starts = items.index(cur_cell)
                cycle_length = len(items) - cycle_starts
                return items[cycle_starts + (N - cycle_starts) % cycle_length]

            items += [cur_cell]
            so_far.add(cur_cell)
            cells = get_next(cells)

        return cells

    def prisonAfterNDaysFromDiscussion(self, cells: List[int], N: int) -> List[int]:
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
    print(s.prisonAfterNDays([0,1,0,1,1,0,0,1], 1))

