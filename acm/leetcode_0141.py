# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None or head.next is None:
            return False
        ptr1 = head.next
        ptr2 = head.next.next
        while True:
            if ptr1 is None or ptr2 is None or ptr2.next is None:
                return False

            if ptr1 is ptr2 :
                return True

            ptr1 = ptr1.next
            ptr2 = ptr2.next.next




# test data
case = [[1,2,3,4,3,2,1]
        ]

# run
solution = Solution()
for (a) in case:
#    result = solution.singleNumber(a)
#    print result
