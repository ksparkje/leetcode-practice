# 4. Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5


'''
꽤 많이 헷갈림... 한번 이해하면 할 만 하다...

중간 값을 찾는 일이나 k번째 값을 찾는 일이나 결국 ...

양쪽을 어떻게 버릴 것 인가에 초점을 두자

예를 들어 4번째 수를 찾는다 하자.
Currently,
A = [1,2,3], B = [1,1,2]
len_A = len_B = 3
middle index = 1

since A[mid] > B[mid], kill the left of B[mid], this is best we can do for now

I am looking for 3rd elem, k = 3
A = [1, 1, 1, 1, 1, 2, 3, 4] => 8 elem
B = [1, 1, 1, 4]             => 4 elem
A_mid = 4, B_mid = 2
A[mid] == B[mid], and since we have k < middle_index_a + middle_index_b,
let's kill the right side of A, keep the same k

https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
'''


def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.


def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2, len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices
    # i.e. k 개를 찾고자 하는데 현재 보고있는 왼쪽의 갯수는 ia + ib...
    # 그러므로 왼쪽에 있는 수 들을 버려야 함...
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            #                    ib + 1개 를 버리는 ...
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            #                 ia + 1개를 버린다...
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    # 이 경우는 k를 왼쪽에서 죽일수 없으니 오른쪽에서 죽이자...
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)

        if total_length % 2:
            return self.find_kth(nums1, nums2, total_length // 2)
        else:
            return (self.find_kth(nums1, nums2, total_length // 2) +
                    self.find_kth(nums1, nums2, total_length // 2 - 1)) / 2

    def find_kth(self, a1, a2, k):
        if not a1:
            return a2[k]
        if not a2:
            return a1[k]

        mid_1 = len(a1)//2
        mid_2 = len(a2)//2

        elem_1 = a1[mid_1]
        elem_2 = a2[mid_2]

        if mid_1 + mid_2 < k:
            if elem_1 < elem_2:
                return self.find_kth(a1[mid_1 + 1:], a2, k - (mid_1 + 1))
            else:
                return self.find_kth(a1, a2[mid_2 + 1:], k - (mid_2 + 1))
        else:
            # This case includes mid1 + mid2 == k
            if elem_1 < elem_2:
                return self.find_kth(a1, a2[:mid_2], k)
            else:
                return self.find_kth(a1[:mid_1], a2, k)
