# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None :
            return 0
        else :
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# test data
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(2)
a.right.left = TreeNode(4)
a.right.right = TreeNode(3)

b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(2)
b.left.right = TreeNode(4)
b.right.right = TreeNode(4)


case = [(a),
        (b)
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.levelOrderBottom(a)
    print result
