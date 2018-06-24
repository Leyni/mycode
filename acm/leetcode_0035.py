# -*- coding: utf-8 -*-

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(0, len(nums)):
            if target <= nums[i] :
                return i
        return len(nums)

# test data
test_data = [
        ([1,3,5,6], 5),
        ([1,3,5,6], 2),
        ([1,3,5,6], 7),
        ([1,3,5,6], 0)
        ]

# run
solution = Solution()
for (case1, case2) in test_data:
    result = solution.searchInsert(case1, case2)
    print (result, case1, case2)
