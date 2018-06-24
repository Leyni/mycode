# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: (int, bool)
        """

        if root is None:
            return (0, True)
        else :

            left = self._isBalanced(root.left)
            right = self._isBalanced(root.right)
            return (max(left[0], right[0]) + 1,
                    left[1] and right[1] and abs(left[0] - right[0]) <= 1)


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True
        else:
            return self._isBalanced(root)[1]

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

case = [(a), (b)
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.isBalanced(a)
    print result
