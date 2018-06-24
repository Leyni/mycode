# -*- coding: utf-8 -*-

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        res = 0
        for i in range(0, len(s)) :
            if i == 0 or roman_dict[s[i - 1]] >= roman_dict[s[i]] :
                res += roman_dict[s[i]]
            else :
                res += roman_dict[s[i]] - 2 * roman_dict[s[i - 1]]

        return res

# test data

# run
solution = Solution()
result = solution.romanToInt("DCXXI")

# output check
print result
