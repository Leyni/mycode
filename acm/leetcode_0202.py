# -*- coding: utf-8 -*-

class Solution(object):
    def trans(self, n):
        res = 0
        while n :
            res += (n % 10) * (n % 10)
            n /= 10
        return res

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        fast = n
        slow = n
        while True:
            slow = self.trans(slow)
            fast = self.trans(fast)
            fast = self.trans(fast)
            if fast == slow:
                break
        return slow == 1

# test data
case = [19,
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.isHappy(a)
    print result
