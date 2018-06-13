# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0;
        j = len(s) - 1
        while i <= j:
            while i < len(s) and not s[i].isalpha() and not s[i].isdigit(): i += 1
            while j >= 0 and not s[j].isalpha() and not s[j].isdigit() : j -= 1
            if i > j : break
            if s[i].lower() != s[j].lower() : break
            i += 1
            j -= 1

        return i > j


# test data
case = ["A man, a plan, a canal: Panama",
        "race a car"
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.isPalindrome(a)
    print result
