# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0 : return False

        y = 0
        z = x
        while z != 0 :
            y = y * 10 + z % 10
            z = z / 10

        if x == y :
            return True
        else :
            return False

# test data

# run
solution = Solution()
result = solution.isPalindrome(1000)

# output check
print result
