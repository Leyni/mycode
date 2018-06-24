# -*- coding: utf-8 -*-

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self._sum = [0]
        for i in range(0, len(nums)):
            self._sum.append(self._sum[i] + nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        return self._sum[j + 1] - self._sum[i]

case = [(0,2),(2,5),(0,5)
        ]

# run
numarray = NumArray([-2, 0, 3, -5, 2, -1])
for (a, b) in case:
    result = numarray.sumRange(a, b)
    print result
