# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = 0
        need_clear = True
        for i in range(0, len(s)):
            if s[i] != ' ' :
                if need_clear :
                    length = 1
                    need_clear = False
                else :
                    length += 1
            else :
                need_clear = True

        return length

# test data
case = 'hello world '

# run
solution = Solution()
result = solution.lengthOfLastWord(case)
print (result)
