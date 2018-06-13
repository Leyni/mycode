# -*- coding: utf-8 -*-

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0
        for i in range(0, len(nums)):
            res ^= nums[i]
        res ^= 0
        return res


# test data
case = [[1,2,3,4,3,2,1]
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.singleNumber(a)
    print result
