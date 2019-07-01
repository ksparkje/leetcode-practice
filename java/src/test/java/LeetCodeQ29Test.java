import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class LeetCodeQ29Test {
    @Test
    public void getAnswer() {
        LeetCodeQ29 s = new LeetCodeQ29();
        assertEquals(10/3, s.divide(10, 3));
        assertEquals(123202/31, s.divide(123202, 31));
        assertEquals(1/1, s.divide(1, 1));
        assertEquals(20/4, s.divide(20, 4));
        assertEquals(-20/4, s.divide(-20, 4));
        assertEquals(21373/2, s.divide(21373, 2));
        assertEquals(2137366/2, s.divide(2137366, 2));
        assertEquals(-2137366/2, s.divide(-2137366, 2));
        assertEquals(-2137366/82, s.divide(-2137366, 82));
    }
}