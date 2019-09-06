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
        p1=p2=head
        while p2 and p1:
            p1=p1.next
            p2=p2.next
            if p2 is None:
                return False
            else:
                p2=p2.next
            if p1==p2:
                return True
        return False
            