import java.util.Arrays;
import java.util.PriorityQueue;

public class LeetCodeQ215 {
    /**
     * Easy question, but the faster version is something to consider...
     */
    public int findKthLargest(int[] nums, int k) {

        if (nums.length == 0 || k <= 0) { return -1; }

        final PriorityQueue<Integer> pq = new PriorityQueue<>();

        Arrays.stream(nums).forEach(item -> pq_push_pop(pq, item, k));

        return pq.peek();
    }

    private void pq_push_pop(PriorityQueue<Integer> pq, Integer item, int pq_size) {
        pq.add(item);
        if (pq.size() > pq_size) { pq.poll(); }
    }

    public int findKthLargestFaster(int[] nums, int k) {
        if (nums == null || nums.length == 0) return -1;
        return findKthHelper(nums, 0, nums.length-1, nums.length - k);

    }

    private int findKthHelper(int[] nums, int start, int finish, int k) {
        if (start > finish) return -1;

        // Use the last elem as pivot
        int pivot = nums[finish];
        int left = start;

        for (int i = start; i < finish; i++) {
            // put everything less than pivot to the left side
            if (nums[i] < pivot) {
                swap(nums, i, left++);
            }
        }
        swap(nums, left, finish);

        if (left == k) {
            return nums[left];
        } else if (left < k) {
            return findKthHelper(nums, left+1, finish, k);
        } else {
            return findKthHelper(nums, start, left-1, k);
        }
    }

    private void swap(int[] nums, int l, int r) {
        int temp = nums[l];
        nums[l] = nums[r];
        nums[r] = temp;
    }

}
