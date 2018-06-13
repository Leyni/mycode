# -*- coding: utf-8 -*-

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        s = ''

        if n == 0:
            return s

        while n:
            s = chr((n - 1) % 26 + ord('A')) + s
            n = (n - 1) / 26

        return s




# test data
case = [1, 2, 3, 26, 27, 28
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.convertToTitle(a)
    print result
