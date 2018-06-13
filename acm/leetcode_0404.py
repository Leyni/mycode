# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root, is_left = False):
        """
        :type root: TreeNode
        :type
        :rtype: int
        """

        if root is None:
            return 0

        return self.sumOfLeftLeaves(root.left, True) \
                + self.sumOfLeftLeaves(root.right, False) \
                + root.val if is_left else 0



case = [1
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.(a)
    print result
