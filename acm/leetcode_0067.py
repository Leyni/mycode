# -*- coding: utf-8 -*-

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = a[::-1]
        b = b[::-1]

        plus = 0
        res = ''
        for i in range(0, max(len(a), len(b))) :
            x = int(a[i]) if i < len(a) else 0
            y = int(b[i]) if i < len(b) else 0
            res += str((x + y + plus) % 2)
            plus = (x + y + plus) / 2
        if plus == 1 :
            res += '1'

        return res[::-1]



# test data
case = [('11', '1'),
        ('1010', '1011')
        ]

# run
solution = Solution()
for (a, b) in case:
    result = solution.addBinary(a, b)
    print (result)
