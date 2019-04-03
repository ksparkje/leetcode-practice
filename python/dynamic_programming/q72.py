# 72. Edit Distance
# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        len_word1, len_word2 = len(word1), len(word2)
        # Use word2 as rows, word1 as columns to build a table
        table = [[-1] * len_word2 for _ in range(len_word1)]

        def compute_table_if_necessary(idx1, idx2):
            ''' return the cost at idx1, idx2'''
            if idx1 < 0:
                return idx2 + 1
            if idx2 < 0:
                return idx1 + 1
            if table[idx1][idx2] == -1:
                if word1[idx1] == word2[idx2]:
                    table[idx1][idx2] = compute_table_if_necessary(idx1-1, idx2-1)
                else:
                    substitute_distance = compute_table_if_necessary(idx1-1, idx2-1)
                    delete_distance     = compute_table_if_necessary(idx1, idx2-1)
                    add_distance        = compute_table_if_necessary(idx1-1, idx2)

                    table[idx1][idx2] = 1 + min((delete_distance, add_distance, substitute_distance))

            return table[idx1][idx2]

        return compute_table_if_necessary(len_word1-1, len_word2-1)

    def epiMinDistance(self, A: str, B: str) -> int:
        def compute_distance_between_prefixes(A_idx, B_idx):
            if A_idx < 0:
                # A is empty so add all of B's characters.
                return B_idx + 1
            elif B_idx < 0:
                # B is empty so delete all of A's characters.
                return A_idx + 1
            if distance_between_prefixes[A_idx][B_idx] == -1:
                if A[A_idx] == B[B_idx]:
                    distance_between_prefixes[A_idx][B_idx] = (
                        compute_distance_between_prefixes(A_idx - 1, B_idx - 1))
                else:
                    substitute_last = compute_distance_between_prefixes(
                        A_idx - 1, B_idx - 1)
                    add_last = compute_distance_between_prefixes(A_idx - 1, B_idx)
                    delete_last = compute_distance_between_prefixes(
                        A_idx, B_idx - 1)
                    distance_between_prefixes[A_idx][B_idx] = (
                        1 + min(substitute_last, add_last, delete_last))
            return distance_between_prefixes[A_idx][B_idx]

        distance_between_prefixes = [[-1] * len(B) for _ in A]
        return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)