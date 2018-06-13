# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0, len(numbers) - 1):
            temp = target - numbers[i]

            s = i + 1
            e = len(numbers) - 1
            while s <= e:
                j = (s + e) / 2
                if temp < numbers[j]:
                    e = j - 1
                elif numbers[j] < temp :
                    s = j + 1
                else:
                    return [i + 1, j + 1]

        return None

# test data
case = [[2, 7, 11, 15]
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.twoSum(a, 9)
    print result
