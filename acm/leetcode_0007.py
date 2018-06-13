# -*- coding: utf-8 -*-
import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        positive = 1 if x >= 0 else -1
        x = x * positive
        y = 0

        while x != 0 :
            y = y * 10 + x % 10
            x = x / 10

        y = y * positive if y <= 2 ** 31 - 1 and y >= -(2 ** 31) else 0

        return y

# test data

# run
solution = Solution()
result = solution.reverse(int(1563847412))

# output check
print result
