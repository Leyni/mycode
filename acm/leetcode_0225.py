# -*- coding: utf-8 -*-

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """

        self._stack.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """

        if self._stack:
            x = self._stack[len(self._stack) - 1]
            self._stack.pop()
            return x
        else:
            return None


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self._stack:
            return self._stack[len(self._stack) - 1]
        else:
            return None


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """

        if self._stack:
            return False
        else:
            return True



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# test data

case = [[1,2,3],[1,2,2]
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.containsNearbyDuplicate(a, 1)
    print result
