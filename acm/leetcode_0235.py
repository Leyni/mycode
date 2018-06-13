# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        while (root.val - p.val) * (root.val - q.val) > 0:
            root = root.left if root.val > p.val else root.right
        return root

# test data

case = [a, b
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.isPalindrome(a)
    print result
