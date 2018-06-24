# -*- coding: utf-8 -*-

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    return 6 - num

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, e, mid = 1, n, (n + 1) / 2
        while s <= e:
            check = guess(mid)
            if check == 0:
                return mid
            elif check > 0:
                s, mid = mid + 1, (e + mid + 1) / 2
            else:
                e, mid = mid - 1, (s + mid - 1) / 2


case = [6,7,8,9,10
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.guessNumber(a)
    print result
