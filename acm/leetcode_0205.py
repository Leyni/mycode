# -*- coding: utf-8 -*-

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        cmap = {}

        for i in range(0, len(s)):
            if cmap.has_key(s[i]):
                if t[i] != cmap[s[i]]:
                    return False
            else:
                if t[i] in cmap.values():
                    return False
                cmap[s[i]] = t[i]

        return True


# test data

case = [('egg', 'add'),
        ('foo', 'bar'),
        ('paper', 'title'),
        ('ab', 'aa'),
        ('ab', 'ca')
        ]

# run
solution = Solution()
for (a, b) in case:
    result = solution.isIsomorphic(a, b)
    print result
