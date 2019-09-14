import java.util.Arrays;
import java.util.function.IntBinaryOperator;
import java.util.function.IntPredicate;
import java.util.stream.IntStream;

/**
260. Single Number III
Medium
984
81
        Given an array of numbers nums, in which exactly two elements appear
         only once and all the other elements appear exactly twice. Find the
         two elements that appear only once.

        Example:

        Input:  [1,2,1,3,2,5]
        Output: [3,5]
        Note:

        The order of the result is not important. So in the above example,
        [5, 3] is also correct.

        Your algorithm should run in linear runtime complexity. Could you
        implement it using only constant space complexity?


    --------
    Solution
    --------
    Obviously bitwise question.
    If we xor all, then the result is the xor of the two unique integers.
    Since result of the xor means the two number differs in the bit with value 1,
    (the turned on value), we find the value with the least bit that's 1 by
    the usual `given & ~(given - 1)
 */


public class LeetCodeQ260 {
    public int[] singleNumber(int[] nums) {
        IntBinaryOperator tComparator = (a, b) -> a ^ b;

        final int xorAll = Arrays.stream(nums)
                                 .reduce(tComparator)
                                 .getAsInt();

        final int lastDigitDiff = xorAll & -xorAll;

        IntPredicate keyEventDispatcher = (value) -> (lastDigitDiff & value) > 0;

        IntStream intStreamNonzero = Arrays.stream(nums)
                                           .filter(keyEventDispatcher);
        IntStream intStreamZero= Arrays.stream(nums)
                                       .filter(keyEventDispatcher.negate());

        return new int[]{intStreamNonzero.reduce(tComparator).getAsInt(),
                         intStreamZero.reduce(tComparator).getAsInt()
        };
    }
}
