# -*- coding: utf-8 -*-

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []

        res = [[1]]
        for i in range(1, numRows):
            temp = []
            temp.append(res[i - 1][0])
            for j in range(1, i):
                temp.append(res[i - 1][j - 1] + res[i - 1][j])
            temp.append(res[i - 1][i - 1])
            res.append(temp)

        return res

# test data
case = [(5)
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.generate(a)
    print result
