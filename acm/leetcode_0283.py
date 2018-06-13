# -*- coding: utf-8 -*-

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        s = e = 0
        while e < len(nums):
            if nums[e]:
                nums[s] = nums[e]
                s += 1
            e += 1
        while s < len(nums):
            nums[s] = 0
            s += 1


case = [[0,1,0,3,12]
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.moveZeroes(a)
    print a
