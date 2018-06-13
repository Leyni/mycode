# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bTreePaths(self, root, path, paths):
        if root.left:
            self.bTreePaths(root.left, path + [root.val], paths)
        if root.right:
            self.bTreePaths(root.right, path + [root.val], paths)
        if root.left is None and root.right is None:
            paths.append('->'.join(str(x) for x in path + [root.val]))

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        path = []
        paths = []
        if root:
            self.bTreePaths(root, path, paths)
        return paths

# test data
a = TreeNode

case = [('anagram', 'nagaram'),('rat', 'car')
        ]

# run
solution = Solution()
for (a, b) in case:
    result = solution.isAnagram(a, b)
    print result
