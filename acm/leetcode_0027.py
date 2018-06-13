# -*- coding: utf-8 -*-

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        for i in range(0, len(nums) - count):
            nums.pop()

        return count

# test data
test_data = [
        ([3,2,2,3], 3),
        ([0,1,2,2,3,0,4,2], 2)
        ]

# run
solution = Solution()
for (case1, case2) in test_data:
    result = solution.removeElement(case1, case2)
    print (result, case1, case2)
