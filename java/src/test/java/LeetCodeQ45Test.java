import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class LeetCodeQ45Test {

    @Test
    void jump() {
//        int [] random_input = new int []{2, 3, 1, 1, 4};
        int [] random_input = {2, 3, 1, 1, 4};

        LeetCodeQ45 s = new LeetCodeQ45();
        assertEquals(2, s.jump(random_input));
    }
}