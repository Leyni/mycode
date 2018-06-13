# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = fast = head
        rev = None
        while fast and fast.next:
            rev, rev.next, slow, fast = slow, rev, slow.next, fast.next.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return rev == None


# test data
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(3)
a.next.next.next.next.next = ListNode(2)
a.next.next.next.next.next.next = ListNode(1)

b = ListNode(0)
b.next = ListNode(2)
b.next.next = ListNode(2)
b.next.next.next = ListNode(1)

case = [a, b
        ]

# run
solution = Solution()
for (a) in case:
    result = solution.isPalindrome(a)
    print result
