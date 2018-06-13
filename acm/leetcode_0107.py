# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        queue = []
        if root is None :
            return res
        else:
            queue.append(root)

        while len(queue) != 0:
            next_queue = []
            val_queue = []

            for i in range(0, len(queue)):
                val_queue.append(queue[i].val)
                if (queue[i].left is not None):
                    next_queue.append(queue[i].left)
                if (queue[i].right is not None):
                    next_queue.append(queue[i].right)

            res.insert(0, val_queue)
            queue = next_queue

        return res


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
