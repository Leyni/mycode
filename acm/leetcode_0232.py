# -*- coding: utf-8 -*-

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack_in = []
        self._stack_out = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """

        self._stack_in.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        x = self.peek()
        self._stack_out.pop()
        return x


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """

        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in[len(self._stack_in) - 1])
                self._stack_in.pop()
        return self._stack_out[len(self._stack_out) - 1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """

        if self._stack_in or self._stack_out:
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
