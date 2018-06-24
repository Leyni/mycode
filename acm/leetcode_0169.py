
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = {}
        for i in range(0, len(nums)):
            if m.has_key(nums[i]):
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1
            if (m[nums[i]] > len(nums) / 2):
                return nums[i]



# test data
case = [[1, 2, 3, 3, 3],[1]
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.majorityElement(a)
    print result
