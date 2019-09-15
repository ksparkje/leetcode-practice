import com.google.common.collect.HashMultiset;
import com.google.common.collect.Multiset;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static java.util.stream.Collectors.toList;

/**
229. Majority Element II
        Medium
        1016
        119

        Given an integer array of size n, find all elements that appear more
        than ⌊ n/3 ⌋ times.

        Note: The algorithm should run in linear time and in O(1) space.

        Example 1:

        Input: [3,2,3]
        Output: [3]

        Example 2:

        Input: [1,1,1,3,3,2,2,2]
        Output: [1,2]

        Accepted
        111.7K
        Submissions
        337.9K


 ----------
 Solution
 ----------

 StefanPochmann: https://leetcode.com/problems/majority-element-ii/discuss/63502/6-lines-general-case-O(N)-time-and-O(k)-space

 I keep up to two candidates in my counter, so this fulfills the O(N) time and O(1) space requirements.

 def majorityElement(self, nums):
     ctr = collections.Counter()
     for n in nums:
        ctr[n] += 1
        if len(ctr) == 3:
            // 이곳에 밑줄 쫙이다...
            ctr -= collections.Counter(set(ctr))
     return [n for n in ctr if nums.count(n) > len(nums)/3]

 Explanation

 Think of it this way: Find three different votes and hide them. Repeat until there
 aren't three different votes left. A number that originally had more than one
 third of the votes now still has at least one vote, because to hide all of its
 votes you would've had to hide more than three times one third of the votes -
 more votes than there were. You can easily have false positives, though, so in
 the end check whether the remaining up to two candidates actually had more than
 one third of the votes.

 My code does just that: Collect (count) the votes for every number, but remove
 triples of three different votes on the fly, as soon as we have such a triple.

 ----------------------------------------------------------
 Generalization to ⌊N/k⌋, still O(N) time but O(k) space
 ----------------------------------------------------------

 For the general problem, looking for elements appearing more than ⌊N/k⌋ times
 for some positive integer k, I just have to change my 3 to k. Then it already
 works and takes takes O(k) space and O(kN) time.

 The O(kN) time does not come from the main loop, though. Yes, each ctr -= ...
 does cost k, but I only have to do it at most N/k times. To put it in terms of
 the above explanation, I can't hide a vote more than once.

 No, the culprit is my last line, counting each remaining candidate separately.
 If I count them at the same time, I get O(N) again. Here's the full generalized code:

 def majorityElement(self, nums, k):
     ctr = collections.Counter()
     for n in nums:
        ctr[n] += 1
        if len(ctr) == k:
           ctr -= collections.Counter(set(ctr))
     ctr = collections.Counter(n for n in nums if n in ctr)
     return [n for n in ctr if ctr[n] > len(nums)/k]

 */


/**
 * Insight: if k == 3, there can only be two different elem at most!
 *
 * Find the first three (since we want k == 3),
 *      increase the count of whichever elem it is.
 * If the number of unique elem is equal to 3,
 *      decrease the count so that we cannot have more than two
 *      unique elems in the possible elems.
 */


public class LeetCodeQ229 {

}













