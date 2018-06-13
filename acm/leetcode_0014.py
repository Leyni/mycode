# -*- coding: utf-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = ""
        if len(strs) == 0 :
            return res

        index = 0
        finish = False
        while True :
            char = None
            for str in strs :
                if index >= len(str) :
                    finish = True
                    break
                if char is None :
                    char = str[index]
                if char != str[index] :
                    finish = True
                    break
            if finish :
                break

            res += char
            index += 1

        return res


# test data
test1 = ["flower","flow","flight"]
test2 = ["dog","racecar","car"]

# run
solution = Solution()
result = solution.longestCommonPrefix(test2)

# output check
print result
