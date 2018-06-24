# -*- coding: utf-8 -*-

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0
        while n :
            res += n & 1
            n >>= 1
        return res


# test data
case = [11,
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.hammingWeight(a)
    print result
