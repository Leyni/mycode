# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root is None :
            return False
        if root.left is None and root.right is None :
            return root.val == sum
        if root.left is None:
            return self.hasPathSum(root.right, sum - root.val)
        if root.right is None:
            return self.hasPathSum(root.left, sum - root.val)

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


# test data
a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(2)
b.left.left = TreeNode(3)
b.left.right = TreeNode(3)
b.left.left.left = TreeNode(4)
b.left.left.right = TreeNode(4)

c = TreeNode(1)
c.left = TreeNode(2)

case = [(a,12), (b,50), (c,3)
        ]

# run
solution = Solution()
for (a, b) in case:
    result = solution.hasPathSum(a, b)
    print result
