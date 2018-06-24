# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetricTree(self, p, q):
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
            if not self.isSymmetricTree(p.left, q.right) :
                return False
            if not self.isSymmetricTree(p.right, q.left) :
                return False

        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None :
            return True
        else:
            return self.isSymmetricTree(root.left, root.right)

# test data
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(2)
a.left.left = TreeNode(3)
a.left.right = TreeNode(4)
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
    result = solution.isSymmetric(a)
    print result
