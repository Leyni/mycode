# -*- coding: utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        l1, l2 = len(nums1), len(nums2)
        (minx, maxx, minl, maxl) = (nums1, nums2, l1, l2) if l1 <= l2 else (nums2, nums1, l2, l1)
        s, e, m = 0, minl, (minl + maxl + 1) >> 1
        m1 = (s + e) >> 1
        m2 = m - m1

        print minx, maxx, l1, l2

        while(True):
            print "iter = %d, %d, %d" % (m, m1, m2)

            if (m1 == 0 or minx[m1 - 1] <= maxx[m2]) and (m1 == minl or maxx[m2 - 1] <= minx[m1]):
                break
            if (m1 != 0 and minx[m1 - 1] > maxx[m2]):
                s, e = s, m1 - 1
            else:
                s, e = m1 + 1, e
            m1 = (s + e) >> 1
            m2 = m - m1
            raw_input()

        print "ans = %d, %d" % (m1, m2)

        if ((minl + maxl) & 1 == 1):
            return max(minx[m1 - 1] if m1 != 0 else float("-inf"), maxx[m2 - 1] if m2 != 0 else float("-inf")) * 1.0
        else:
            return (
                    max(minx[m1 - 1] if m1 != 0 else float("-inf"), maxx[m2 - 1] if m2 != 0 else float("-inf"))
                    + min(minx[m1] if m1 != minl else float("inf"), maxx[m2] if m2 != maxl else float("inf"))
                    ) * 0.5


# run
solution = Solution()
case = [
        [[1], [2,3,4]],
        [[1], [1]],
        [[2], []],
        [[], [2,3]],
        [[2,3],[4,5]],
        [[1,3],[2]]
        ]
for (a, b) in case:
    result = solution.findMedianSortedArrays(a, b)
    print result
