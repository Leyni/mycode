# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        ptr = ListNode(None)
        ptr.next = head

        while ptr.next is not None :
            if ptr.val == ptr.next.val :
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next

        return head

# test data
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(2)

b = ListNode(1)
b.next = ListNode(1)
b.next.next = ListNode(2)
b.next.next.next = ListNode(3)
b.next.next.next.next = ListNode(3)

case = [a,
        b]

# run
solution = Solution()
for (a) in case:
    result = solution.deleteDuplicates(a)
    while result is not None:
        print result.val
        result = result.next
