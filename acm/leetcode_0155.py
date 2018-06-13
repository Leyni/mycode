# -*- coding: utf-8 -*-

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        if not self._min_stack or self._min_stack[len(self._min_stack) - 1] >= x:
            self._min_stack.append(x)


    def pop(self):
        """
        :rtype: void
        """

        if len(self._stack):
            if (self._stack[len(self._stack) - 1] == self._min_stack[len(self._min_stack) - 1]):
                self._min_stack.pop()
            self._stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self._stack):
            return self._stack[len(self._stack) - 1]
        else:
            return None


    def getMin(self):
        """
        :rtype: int
        """
        if len(self._min_stack):
            return self._min_stack[len(self._min_stack) - 1]
        else:
            return None

    def prints(self):
        print self._stack
        print self._min_stack


# Your MinStack object will be instantiated and called as such:

minStack = MinStack();
minStack.push(-2); minStack.prints();
minStack.push(0); minStack.prints();
minStack.push(-3); minStack.prints();
minStack.getMin(); minStack.prints();
minStack.pop(); minStack.prints();
minStack.top(); minStack.prints();
minStack.getMin(); minStack.prints();
