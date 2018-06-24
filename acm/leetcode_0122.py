# -*- coding: utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        delta = [0]
        for i in range(1, len(prices)):
            delta.append(prices[i] - prices[i - 1])

        res = 0
        for i in range(1, len(prices)):
            if delta[i] > 0 :
                res += delta[i]

        return res


# test data
case = [[7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1]
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.maxProfit(a)
    print result
