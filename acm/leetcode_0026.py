# -*- coding: utf-8 -*-
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        pre = None
        for i in range(0, len(nums)):
            if pre != nums[i]:
                nums[count] = nums[i]
                pre = nums[i]
                count += 1
        for i in range(0, len(nums) - count):
            nums.pop()

        return count


# test data
test_data = [
        [1,1,2],
        [0,0,1,1,1,2,2,3,3,4]
        ]

# run
solution = Solution()
for case in test_data:
    result = solution.removeDuplicates(case)
    print (result, case)
