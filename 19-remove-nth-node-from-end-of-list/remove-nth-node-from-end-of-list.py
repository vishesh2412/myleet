class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return head
        temp=head
        i=0
        while(temp):
            i+=1
            temp=temp.next
        target=i-n
        if target==0:
            return head.next
        i=0
        temp=head
        while(i<target):
            prev=temp
            temp=temp.next
            i+=1
        prev.next=temp.next
        return head