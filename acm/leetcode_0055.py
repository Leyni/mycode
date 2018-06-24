# -*- coding: utf-8 -*-

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        p = 0
        s = nums[0]
        l = len(nums)
        while (True):
            if s == 0 or p == l - 1:
                break
            p += 1
            s = max(nums[p], s - 1)

        return p == l - 1


# run
solution = Solution()
case = [
        [2,3,1,1,4],
        [3,2,1,0,4]
        ]
for (a) in case:
    result = solution.canJump(a)
    print result
