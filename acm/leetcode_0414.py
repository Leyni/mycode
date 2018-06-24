# -*- coding: utf-8 -*-

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = []
        for x in nums:
            if not x in l:
                l.append(x)
                l.sort()
                l.reverse()
            if len(l) > 3:
                l.pop()

        print l
        if len(l) == 3:
            return l[2]
        elif len(l) == 0:
            return None
        else:
            return l[0]


case = [[1,2]
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.thirdMax(a)
    print result
