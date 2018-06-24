# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA is None or headB is None:
            return None

        ptr1 = headA
        ptr2 = headB
        len1 = 0 if ptr1 is None else 1
        len2 = 0 if ptr2 is None else 1
        if ptr1 is not None:
            while ptr1.next is not None:
                ptr1 = ptr1.next
                len1 += 1
        if ptr2 is not None:
            while ptr2.next is not None:
                ptr2 = ptr2.next
                len2 += 1

        if ptr1.val != ptr2.val :
            return None

        ptr1 = headA
        ptr2 = headB
        if len1 > len2 :
            for i in range(0, len1 - len2) :
                ptr1 = ptr1.next
        else:
            for i in range(0, len2 - len1) :
                ptr2 = ptr2.next

        while ptr1.val != ptr2.val :
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1



# test data
a = ListNode(1)
a.next = ListNode(3)
a.next.next = ListNode(5)
a.next.next.next = ListNode(6)
a.next.next.next.next = ListNode(7)
a.next.next.next.next.next = ListNode(8)
a.next.next.next.next.next.next = ListNode(9)
a.next.next.next.next.next.next.next = ListNode(10)
b = ListNode(2)
b.next = ListNode(4)
b.next.next = ListNode(6)
b.next.next.next = ListNode(7)
b.next.next.next.next = ListNode(8)
b.next.next.next.next.next = ListNode(9)
b.next.next.next.next.next.next = ListNode(10)
case = [(a, b)
        ]

# run
solution = Solution()
for (a, b) in case:
    result = solution.getIntersectionNode(a, b)
    print result.val
