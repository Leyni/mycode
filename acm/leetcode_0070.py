# -*- coding: utf-8 -*-

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = range(0, n + 2)
        res[1] = 1
        res[2] = 2
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]
            print (i, res[i])

        return res[n]

# test data
case = [4,
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.climbStairs(a)
    print (result)
