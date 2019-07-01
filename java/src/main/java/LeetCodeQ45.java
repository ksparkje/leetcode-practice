public class LeetCodeQ45 {
    public int jump(int[] nums) {
        int num_jumps = 0, cur_end = 0, cur_furthest = 0;
        for (int cur_index = 0; cur_index < nums.length - 1; cur_index++) {
            cur_furthest = Math.max(cur_furthest, cur_index + nums[cur_index]);
            if (cur_end == cur_index) {
                cur_end = cur_furthest;
                num_jumps++;
            }
        }
        return num_jumps;
    }
}
