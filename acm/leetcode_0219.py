# -*- coding: utf-8 -*-

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        s = {}
        for i in range(0, len(nums)):
            if s.has_key(nums[i]):
                if i - s[nums[i]] <= k:
                    return True
            s[nums[i]] = i

        return False

# test data

case = [[1,2,3],[1,2,2]
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.containsNearbyDuplicate(a, 1)
    print result
