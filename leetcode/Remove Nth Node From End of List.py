class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1=head
        p2=head
        count=0
        while p2.next is not None:
            p2=p2.next
            count+=1
        for _ in range(count-n):
            p1=p1.next
        if n==0:
            p1.next=None
        else:
            p1.next=p1.next.next    
        return head

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
head=ListNode(None)

A=ListNode(1)
B=ListNode(2)
C=ListNode(3)
D=ListNode(4)
E=ListNode(5)
head.next=A
A.next=B
B.next=C
C.next=D
D.next=E
abc=Solution()
ans=abc.removeNthFromEnd(head,2)
