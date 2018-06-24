# -*- coding: utf-8 -*-

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0 :
            return 0
        elif len(nums) == 1:
            return nums[0]

        norob0 = 0
        rob0 = nums[0]
        norob1 = nums[0]
        rob1 = nums[1]
        m = max(norob1, rob1)
        for i in range(2, len(nums)):
            print (norob0, rob0, norob1, rob1)
            norob0, rob0, norob1, rob1 = norob1, rob1, max(norob1, rob1), norob1 + nums[i]
            m = max(norob1, rob1)

        return m


# test data
case = [[1,2,3,4,5,6,7],
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.rob(a)
    print result
