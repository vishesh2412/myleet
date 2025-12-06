class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return head
        dummy=ListNode(0,head)

        t1=dummy
        t2=dummy

        for i in range(n+1):
            t1=t1.next

        while t1:
            t1=t1.next
            t2=t2.next

        t2.next=t2.next.next

        # return head
        return dummy.next