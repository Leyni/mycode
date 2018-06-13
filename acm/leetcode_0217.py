# -*- coding: utf-8 -*-

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        s = {}
        for i in range(0, len(nums)):
            if s.has_key(nums[i]):
                return True
            else:
                s[nums[i]] = True
        return False

# test data

case = [[1,2,3],[1,2,2]
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.containsDuplicate(a)
    print result
