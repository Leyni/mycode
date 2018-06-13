# -*- coding: utf-8 -*-

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits[len(digits) - 1] += 1

        for i in range(len(digits) - 1, 0, -1) :
            digits[i - 1] += digits[i] / 10
            digits[i] %= 10

        if digits[0] > 9 :
            digits[0] %= 10
            digits.insert(0, 1)

        return digits


# test data
case = [9,9,9]

# run
solution = Solution()
result = solution.plusOne(case)
print (result)
