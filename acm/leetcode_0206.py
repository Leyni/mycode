# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        ptr = head
        head = ListNode(0)
        while ptr:
            cur_ptr = ptr
            ptr = ptr.next
            cur_ptr.next = head.next
            head.next = cur_ptr

        return head.next

# test data
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)

case = [a
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.reverseList(a)
    while result:
        print result.val
        result = result.next
