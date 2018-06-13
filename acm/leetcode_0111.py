# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root.left is None and root.right is None:
            return 1
        else:
            if root.left is None:
                return self.minDepth(root.right) + 1
            elif root.right is None:
                return self.minDepth(root.left) + 1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

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

case = [(a), (b), (c)
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.minDepth(a)
    print result
