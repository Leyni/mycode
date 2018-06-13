# -*- coding: utf-8 -*-


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = nums[0]
        max = nums[0]
        for i in range(1, len(nums)):
            if sum > 0 :
                sum += nums[i]
            else :
                sum = nums[i]
            if sum > max :
                max = sum

        return max

# test data
case = [-2,1,-3,4,-1,2,1,-5,4]

# run
solution = Solution()
result = solution.maxSubArray(case)
print (result)
