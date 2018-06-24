# -*- coding: utf-8 -*-

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        while m < len(nums1) : nums1.pop()
        while n < len(nums2) : nums2.pop()

        i = 0
        j = 0
        while j < len(nums2) :
            if i == len(nums1) or nums2[j] <= nums1[i] :
                nums1.insert(i, nums2[j])
                j += 1
            elif i < len(nums1) :
                i += 1

# test data
case = [([1,2,3], 3, [2,4], 2),
        ([0], 0, [1], 1)
        ]

# run
solution = Solution()
for (a, b, c, d) in case:
    result = solution.merge(a, b, c, d)
    print a
