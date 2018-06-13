# -*- coding: utf-8 -*-

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        s = str.split(' ')
        if len(s) != len(pattern):
            return False

        m1, m2= {}, {}
        for i in range(0, len(s)):
            if m1.has_key(pattern[i]):
                if m1[pattern[i]] != s[i]:
                    return False
            else:
                if m2.has_key(s[i]):
                    return False
                else:
                    m1[pattern[i]] = s[i]
                    m2[s[i]] = pattern[i]
        return True


case = [("abba", "dog cat cat dog"), ("abba", "dog cat cat fish"),
        ("aaaa", "dog cat cat dog"), ("abba", "dog dog dog dog"),
        ]

# run
solution = Solution()
for (a, b) in case:
    result = solution.wordPattern(a, b)
    print result
