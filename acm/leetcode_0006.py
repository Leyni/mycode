# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        step = [numRows * 2 - 2 if numRows != 1 else 1, 0]
        ans = ""
        for i in range(numRows):
            j, p = i, 0
            while j < len(s):
                ans += s[j]
                if step[p] == 0:
                    p = (p + 1) & 1
                j, p = j + step[p], (p + 1) & 1
                print i, j, p, ans, step
                raw_input()
            step = [step[0] - 2, step[1] + 2]
        return ans

case = [
        #["PAYPALISHIRING",3],
        #["PAYPALISHIRING", 4]
        ["A", 1]
        ]

# run
solution = Solution()
for (a,b) in case:
    result = solution.convert(a, b)
    print result
