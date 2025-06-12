class Solution(object):
    def deleteDuplicates(self, head):
        if head==None or head.next==None:
            return head
        new=ListNode(0)
        new.next=head
        temp=new
        while(head!=None and head.next!=None):
            if head.val==head.next.val:
                value=head.val
                while(head.next!=None and head.next.val==value):
                    head=head.next
                temp.next=head.next
            else:
                temp=head
            head=head.next
        return new.next