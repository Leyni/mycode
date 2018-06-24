# -*- coding: utf-8 -*-

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            if root.left:
                root.left.next = root.right
                root.right.next = root.next.left if root.next else root.next
            self.connect(root.left)
            self.connect(root.right)

# run
solution = Solution()
case = [[1,2]
        ]
for (a) in case:
    result = solution.thirdMax(a)
    print result
