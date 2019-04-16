# 11. Container With Most Water
#
# Given n non-negative integers a1, a2, ..., an , where each represents a
# point at coordinate (i, ai). n vertical lines are drawn such that the two
# endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
# with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

# Insight:
#   If we start from the whole thing,
#   the area's length decreases as we move to the other side.
#   Therefore, our height must be greater as we move along

# Start with i, j = 0, len(seq) - 1
# Move i if height[i] < height[j] else j

class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        i, j, so_far = 0, len(height) - 1, 0

        while i < j:
            if height[i] < height[j]:
                so_far, i = max(so_far, (j-i)*height[i]), i+1
            else:
                so_far, j = max(so_far, (j-i)*height[j]), j-1

        return so_far
