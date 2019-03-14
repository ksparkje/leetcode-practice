# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# 
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!


from functools import reduce

# Game plan
#   Start from the left side, walk until we find increasing blocks with respective heights.
#   Do the reverse. Then we know the minimum heights on both sides.
class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        len_height = len(height)
        from_left_increasing = [0 for _ in range(len_height)]
        from_right_increasing = [0 for _ in range(len_height)]
        
        left_min = height[0]
        for idx, h in enumerate(height):
            left_min = max(left_min, h)
            from_left_increasing[idx] = left_min
        
        right_min = height[len_height - 1]
        for idx, h in enumerate(reversed(height)):
            right_min = max(right_min, h)
            from_right_increasing[idx] = right_min

        total_min = [min(left, right) for left, right 
                                        in zip(from_left_increasing, reversed(from_right_increasing))]
        return [h - cur_min for cur_min, h in zip(total_min, height)]
            
        
