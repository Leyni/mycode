# -*- coding: utf-8 -*-

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        s, t = sorted(s), sorted(t)
        for i in range(0, len(s)):
            if s[i] != t[i]:
                return False
        return True



# test data

case = [('anagram', 'nagaram'),('rat', 'car')
        ]

# run
solution = Solution()
for (a, b) in case:
    result = solution.isAnagram(a, b)
    print result
