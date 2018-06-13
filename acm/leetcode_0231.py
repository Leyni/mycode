# -*- coding: utf-8 -*-

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return False
        if n == 1 or n == 2:
            return True

        while n != 1:
            if n & 1:
                return False
            else:
                n >>= 1

        return True


# test data

case = [[1,2,3],[1,2,2]
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.containsNearbyDuplicate(a, 1)
    print result
