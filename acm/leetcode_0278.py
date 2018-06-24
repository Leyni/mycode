# -*- coding: utf-8 -*-

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    x = [None, 0,0,0,1,1,1,1,1]
    return x[version]

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        s, e, mid = 1, n, n / 2
        while s < e:
            print (s, e, mid)
            if isBadVersion(mid):
                e, mid = mid, (s + mid) / 2
            else:
                s, mid = mid + 1, (mid + e) / 2

        return s

case = [4,5,6,7,8
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.firstBadVersion(a)
    print result
