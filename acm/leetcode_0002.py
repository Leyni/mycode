# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        ptr = head

        while l1 is not None or l2 is not None:
            if l1 is None : l1 = ListNode(0)
            if l2 is None : l2 = ListNode(0)

            plus = (ptr.val + l1.val + l2.val) / 10
            ptr.val = (ptr.val + l1.val + l2.val) % 10

            if plus != 0 or l1.next is not None or l2.next is not None:
                ptr.next = ListNode(plus)

            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next

        return head

# test data
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
#l2.next.next = ListNode(7)

# run
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# output check
ptr = result
while ptr is not None :
    print ptr.val
    ptr = ptr.next
