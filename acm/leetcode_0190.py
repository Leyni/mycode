# -*- coding: utf-8 -*-

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = 0
        for i in range(0, 32):
            m = m * 2 + n % 2
            n /= 2
        return m


# test data
case = [43261596,
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.reverseBits(a)
    print result
