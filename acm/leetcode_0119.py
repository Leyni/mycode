# -*- coding: utf-8 -*-
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        res = [1]
        for i in range(0, rowIndex):
            res.append(res[i])
            for j in range(i, 0, -1):
                res[j] = res[j - 1] + res[j]

        return res
