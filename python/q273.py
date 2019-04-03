# 273. Integer to English Words
# Hard
#
# Convert a non-negative integer to its english words representation. Given input is guaranteed to be
# less than 231 - 1.

# Example 1:
#
# Input: 123
# Output: "One Hundred Twenty Three"
#
# Example 2:
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
# Example 4:
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
from typing import List


'''
The Question looks boring, but when we think about the 
best implementation, it can get beautiful.

This is from the `discussion`
'''
class Solution:
    def numberToWords(self, num: int) -> str:
        # purposely add zero, then ignore
        to19 = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def words(n) -> List:
            if n == 0:
                return []
            if n < 20:
                # List operation purposely to return a list
                return to19[n:n+1]
            if n < 100:
                return [tens[n // 10 - 2]] + words(n % 10)
            if n < 1000:
                return [to19[n // 100]] + ['Hundred'] + words(n % 100)

            for power, word in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000 ** (power+1):
                    return words(n // (1000 ** power)) + [word] + words(n % (1000 ** power))
        return ' '.join(words(num)) or 'Zero'

