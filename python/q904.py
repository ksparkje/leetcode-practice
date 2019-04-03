# 904. Fruit Into Baskets
#
# In a row of trees, the i-th tree produces fruit with type tree[i].
#
# You start at any tree of your choice, then repeatedly perform the following steps:
#
# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must
# perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
#
# You have two baskets, and each basket can carry any quantity of fruit, but you want each
# basket to only carry one type of fruit each.
#
# What is the total amount of fruit you can collect with this procedure?

# Example 1:
#
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].

# Example 2:
#
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].

# Example 3:
#
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].

# Example 4:
#
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.


'''
Question is super weirdly worded...
Essentially, you start with two baskets. Each of which can only hold one type of fruit
without limits to how many. So, at max, we can have two different types of fruits.

The question is, start from any node, walk right until you hit more than two different
types of fruits. Figure out the max number of fruits you'd have by starting from any node!
------------------------------------------------------------------------------------------

I think it's a straight forward question, but twisted, as noted in the bottom.
Lets say I start from index 0. Walk right until I have more than two. As soon as I have
the third fruit, I count how many I've had so far, and pop off the one that was seen
the earlier (of the two).
For example, [1, 1, 2, 3] -> start with 0 so, 1, 1, 2. When 3 is seen, pop the fruit 1,
because 1 is seen earlier than 2. Then do the same again.

Note:
The interesting part is that when I keep the max counts, it's best to keep the current
counter and right counter separate. As soon as fruit positions switch, I need to reset
the right counter!

'''

class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        first_fruit = -1
        second_fruit = -1

        total_max = 0
        cur_max = 0
        right_counts = 0

        for fruit in tree:
            if fruit in (first_fruit, second_fruit):
                cur_max += 1
                if fruit == first_fruit:
                    first_fruit, second_fruit = second_fruit, first_fruit
                    right_counts = 1
                else: # fruit == second_fruit
                    right_counts += 1
            else: # It's the new fruit!
                cur_max = right_counts + 1
                right_counts = 1
                first_fruit, second_fruit = second_fruit, fruit

            total_max = max(total_max, cur_max)

        return total_max


















































