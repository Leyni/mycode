# -*- coding: utf-8 -*-

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit, threshold, count = 1, 10, 0

        while n - count > (threshold - 1 - threshold / 10) * digit:
            count += (threshold - threshold / 10) * digit
            digit += 1
            threshold = threshold * 10
        num = (n - count - 1) / digit + threshold / 10
        print (count, digit, threshold, num)
        count += (num - threshold / 10 + 1) * digit
        print (count, digit, threshold, num)
        count = count - n
        print (count, digit, threshold, num)
        while count:
            count -= 1
            num /= 10
        return num % 10

case = [3,11, 100000000
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.findNthDigit(a)
    print result
