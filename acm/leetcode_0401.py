# -*- coding: utf-8 -*-

class Solution(object):
    def product(self, length, count, path, paths):
        if length:
            self.product(length - 1, count, path << 1, paths)
            if count:
                self.product(length - 1, count - 1, (path << 1) + 1, paths)
        else:
            if count == 0:
                paths.append(path)

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """


        paths = []
        self.product(10, num, 0, paths)

        ans = []
        for bits in paths:
            minutes = bits & 63
            hours = bits >> 6 & 15
            if minutes < 60 and hours < 12:
                ans.append(("%d" % hours) + ':' + ("%02d" % minutes))

        return ans


case = [1
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.readBinaryWatch(a)
    print result
