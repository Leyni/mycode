# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None or q is None) :
            if p is not None or q is not None:
                return False
        else :
            if p.val != q.val :
                return False
            if not self.isSameTree(p.left, q.left) :
                return False
            if not self.isSameTree(p.right, q.right) :
                return False

        return True

# test data
a1 = TreeNode(1)
a1.left = TreeNode(2)
a1.right = TreeNode(3)
b1 = TreeNode(1)
b1.left = TreeNode(2)
b1.right = TreeNode(3)

a2 = TreeNode(1)
a2.left = TreeNode(2)
b2 = TreeNode(1)
b2.right = TreeNode(2)

a3 = TreeNode(1)
a3.left = TreeNode(2)
a3.right = TreeNode(1)
b3 = TreeNode(1)
b3.left = TreeNode(1)
b3.right = TreeNode(2)

case = [(a1, b1),
        (a2, b2),
        (a3, b3)
        ]

# run
solution = Solution()
for (a, b) in case:
    result = solution.isSameTree(a, b)
    print result
