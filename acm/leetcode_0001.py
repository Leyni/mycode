# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_dict = {}

        for index, number in enumerate(nums) :
            delta = target - number
            if nums_dict.has_key(delta) :
                return [nums_dict[delta], index]
            else :
                nums_dict[number] = index

        return None


nums = [1, 3, 4, 5, 6, 9, 0, 8, 4, 6]
target = 9

solution = Solution()

print(solution.twoSum(nums, target))
