# -*- coding: utf-8 -*-

class Stack(object):
    def __init__(self):
        self.data = []
        self.count = 0
    def isEmpty(self):
        if self.count == 0 :
            return True
        else:
            return False
    def push(self, item):
        self.data.append(item)
        self.count += 1
    def pop(self):
        if self.count != 0:
            self.data.pop()
            self.count -= 1
    def top(self):
        if self.count != 0:
            return self.data[self.count - 1]
        else:
            return None

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()

        left_set = set(['(', '[', '{'])
        right_set = set([')', ']', '}'])
        lr_dict = {')':'(', ']':'[', '}':'{'}

        is_bad = False
        for i in range(0, len(s)):
            if s[i] in left_set :
                stack.push(s[i])
            elif s[i] in right_set :
                if stack.top() != lr_dict[s[i]]:
                    is_bad = True
                    break
                stack.pop()
            else:
                is_bad = True
                break

        return stack.isEmpty() and not is_bad


# test data
test_data = ["()", "()[]{}", "(]", "([)]", "{[]}", "", "]"]

# run
solution = Solution()
for case in test_data :
    result = solution.isValid(case)
    print (case, result)
