import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class LeetCodeQ260Test {

    private LeetCodeQ260 l;

    @BeforeEach
    public void setups() { l = new LeetCodeQ260(); }

    @Test
    void getUniqueNumbers() {
        int[] givenIntegers = {1, 2, 3, 4, 3, 4};

        System.out.println(Arrays.toString(l.singleNumber(givenIntegers)));
    }

}