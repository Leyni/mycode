# -*- coding: utf-8 -*-

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        for i in range(0, len(s)):
            num = num * 26 + ord(s[i]) - ord('A') + 1
        return num

# test data
case = ['A', 'B', 'C', 'Z', 'AA', 'AB'
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.titleToNumber(a)
    print result
