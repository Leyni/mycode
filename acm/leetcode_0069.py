# -*- coding: utf-8 -*-

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0 or x == 1:
            return x

        s = 1
        e = x
        m = (s + e) / 2

        while True:
            if (m * m) <= x and (m + 1) * (m + 1) > x :
                break
            if (m * m) > x :
                e = m
                m = (s + e) / 2
                continue
            if (m + 1) * (m + 1) <= x :
                s = m
                m = (s + e) / 2
                continue

        return m


# test data
case = [4,
        8,
        16,
        15,
        17
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.mySqrt(a)
    print (result, a)
