# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        ptr = head
        while l1 is not None or l2 is not None :
            if l1 is None :
                ptr.next = l2
                l2 = l2.next
                ptr = ptr.next
                continue
            if l2 is None :
                ptr.next = l1
                l1 = l1.next
                ptr = ptr.next
                continue

            if l1.val < l2.val :
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next

        return head.next


# test data
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(5)

# run
solution = Solution()
result = solution.mergeTwoLists(l1, l2)

# check
while result is not None:
    print result.val
    result = result.next
