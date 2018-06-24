# -*- coding: utf-8 -*-

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num >= 10:
            s = 0
            while num:
                s += num % 10
                num /= 10
            num = s

        return num


# test data
a = TreeNode

case = [('anagram', 'nagaram'),('rat', 'car')
        ]

# run
solution = Solution()
for (a, b) in case:
    result = solution.isAnagram(a, b)
    print result
