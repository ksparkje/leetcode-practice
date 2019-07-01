import org.junit.Before;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class LeetCodeQ215Test {

    private LeetCodeQ215 l;

    @BeforeEach
    public void setups() { l = new LeetCodeQ215(); }


    @Test
    void findKthLargest() {

        int [] test_input = new int[]{1,2,3,4,5};
        assertEquals(l.findKthLargest(test_input, 3), 3);

        int [] test_input_2 = new int[]{};
        assertEquals(l.findKthLargest(test_input_2, 0), -1);
    }

    @Test
    void findKthLargestFaster() {

        int [] test_input = new int[]{1,2,3,4,5};
        assertEquals(l.findKthLargestFaster(test_input, 3), 3);

        int [] test_input_2 = new int[]{};
        assertEquals(l.findKthLargestFaster(test_input_2, 0), -1);
    }
}