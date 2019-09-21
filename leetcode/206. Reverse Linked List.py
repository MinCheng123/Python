class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer=head
        start=True     
        if head is None:
            return None
        if head.next is None:
            return head
        while head.next:
            pointer=head.next
            if start:
                head.next= None
                start=False
            else:
#                head=pointer
                head.next=previous
            previous=head
            head=pointer
        head.next=previous
        return head

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

A=ListNode(1)
B=ListNode(2)
C=ListNode(3)
D=ListNode(4)
E=ListNode(5)
A.next=B
B.next=C
C.next=D
D.next=E

abc=Solution()
abc.reverseList( A)