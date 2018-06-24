# -*- coding: utf-8 -*-

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)


# test data
case = [1000
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.trailingZeroes(a)
    print result
