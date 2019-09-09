
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        if head is None:
            return None
        p = head
        flag=1
        # while p:

        #     if p.next and p.next.next and p.next.next.next:
        #         p1=p.next
        #         p2=p.next.next
        #         p3=p.next.next.next

        #         p.next=p2
        #         p2.next=p1
        #         p1.next =p3
                
        #         p=p.next.next

                
                
        #     elif p.next and p.next.next:
        #         p1=p.next
        #         p2=p.next.next
        #         p.next=p2
        #         p2.next=p1
        #         p1.next= None
        #         p=p.next.next
        #     else:
        #         break
         


        # return head

        first=1
        while p:
            if p.next and p.next.next:

                if first ==1:
                    p1=p
                    p2=p.next
                    p3=p.next.next
                    p1.next=p3
                    p2.next=p1
                    head=p2
                    p=p2
                    first = 0
                elif  p.next and p.next.next and p.next.next.next:
                    p1=p.next
                    p2=p.next.next
                    p3=p.next.next.next

                    p.next=p2
                    p2.next=p1
                    p1.next =p3
                    
                    p=p.next.next
                    p1=p
                    p2=p.next
                    p3=p.next.next
                    p.next=p2
                    p2.next=p1
                    p1.next =p3
                    p=p3
            else:
                break
        return head
#                 p2.next=p1
#                 p1.next =p3




class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#head=ListNode(-1)
A=ListNode(1)
B=ListNode(2)
C=ListNode(3)
D=ListNode(4)
#head.next=A
A.next=B
B.next=C
C.next=D
abc=Solution()
answer=abc.swapPairs(A)
print(answer)