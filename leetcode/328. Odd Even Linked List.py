class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        even=ListNode(-1)
        even_head=even
        odd =ListNode(-2)
        odd_head=odd
        isodd=True
        while head.next:
            if isodd==True:
                odd.next=head
                odd=odd.next
                isodd=False
            else:
                isodd=True
                even.next=head
                even=even.next
            head=head.next
        if isodd==True:
            odd.next=head
            even.next=None
            odd=odd.next
        else:
            even.next=head
            odd.next=None
            
        odd.next=even_head.next
        return odd_head.next
            
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
abc.oddEvenList( A)