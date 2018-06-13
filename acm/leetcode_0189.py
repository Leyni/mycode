# -*- coding: utf-8 -*-

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = i
        temp = nums[i]
        times = len(nums)
        while times :
            j = j + k if j + k < len(nums) else (j + k) % len(nums)
            nums[j], temp = temp, nums[j]
            if i == j :
                i = i + 1 if i + 1 < len(nums) else 0
                j = i
                temp = nums[i]
            times -= 1

# test data
case = [([1,2,3,4,5,6,7], 3),
        ([-1], 2),
        ([1, 2], 1)
        ]

# run
solution = Solution()
for (a, b) in case:
    solution.rotate(a, b)
    print a
