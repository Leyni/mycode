 -*- coding: utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        m = {}
        for x in list(s):
            if m.has_key(x):
                count += 1
                m.pop(x)
            else:
                m[x] = 1

        count += count + (1 if len(m) else 0)

        return count


case = ["abccccdd"
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.longestPalindrome(a)
    print result
