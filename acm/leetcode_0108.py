# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        left = nums[0 : len(nums) / 2]
        right = nums[len(nums) / 2 + 1 :]

        root = TreeNode(nums[len(nums) / 2]) if nums else None
        if left :
            root.left = self.sortedArrayToBST(left)
        if right :
            root.right = self.sortedArrayToBST(right)

        return root


# test data
case = [([-10,-3,0,5,9])
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.sortedArrayToBST(a)
    print result.left.val
