# -*- coding: utf-8 -*-

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        bit = 0
        for x in nums:
            bit |= 1 << x

        res = 0
        while bit and bit & 1 == 1:
            bit, res = bit / 2, res + 1

        return res

# test data

case = [([3,0,1]),([9,6,4,2,3,5,7,0,1])
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.missingNumber(a)
    print result
