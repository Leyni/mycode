# -*- coding: utf-8 -*-

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1 :
            return '1'
        else :
            s = self.countAndSay(n - 1)

            pre = s[0]
            count = 1
            res = ''
            for i in range(1, len(s)):
                if pre != s[i] :
                    res += str(count) + pre
                    pre = s[i]
                    count = 1
                else:
                    count += 1

            res += str(count) + pre

            return res

# test data

# run
solution = Solution()
result = solution.countAndSay(5)
print (result)
