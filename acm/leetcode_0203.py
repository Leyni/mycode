# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        pre_head = ListNode(0)
        pre_head.next = head
        pre_ptr = pre_head
        ptr = head
        while ptr:
            if ptr.val == val:
                pre_ptr.next = ptr.next
            else :
                pre_ptr = pre_ptr.next
            ptr = ptr.next

        return pre_head.next

# test data
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(6)
a.next.next.next = ListNode(5)

case = [a,
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.removeElements(a, 6)
    while result:
        print result.val
        result = result.next
