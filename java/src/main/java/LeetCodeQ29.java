public class LeetCodeQ29 {
    /*
    Leetcode 29. Error out for -(1<<32-1), but for a record...
     */
    public int divide(int dividend, int divisor) {
        int total = 0;
        int count = 0;
        boolean isNeg = (dividend < 0 || divisor < 0) && !(dividend < 0 && divisor < 0);

        if (dividend < 0) { dividend = -dividend; }
        if (divisor < 0) { divisor = -divisor; }

        if (divisor == 1) { return isNeg ? -dividend : dividend; }
        if (dividend <= divisor) { return dividend == divisor ? 1 : 0; }

        while (dividend - (divisor << count) > 0) { count++; }

        total = divideHelper(dividend, divisor, count, total);

        return isNeg ? -total : total;
    }

    private int divideHelper(int dividend, int divisor, int count, int total) {
        if (dividend <= 0 || count < 0) {
            return total;
        }

        if (dividend >= (divisor << count)) {
            total += 1 << count;
            dividend -= (divisor << count);
        }
        count--;
        return divideHelper(dividend, divisor, count, total);
    }

    public int sampleSolution(int A, int B) {
        if (A == 1 << 31 && B == -1) return (1 << 31) - 1;
        int a = Math.abs(A), b = Math.abs(B), res = 0, x = 0;
        while (a - b >= 0) {
            for (x = 0; a - (b << x << 1) >= 0; x++);
            res += 1 << x;
            a -= b << x;
        }
        return (A > 0) == (B > 0) ? res : -res;
    }
}

