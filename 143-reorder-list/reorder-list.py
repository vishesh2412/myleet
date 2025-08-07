# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return None
        slow,fast=head,head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next

        middle=None
        temp=slow.next
        slow.next=None
        while(temp):
            new=temp.next
            temp.next=middle
            middle=temp
            temp=new

        first=head
        second=middle
        while(second):
            temp1=first.next
            temp2=second.next
            
            first.next=second
            second.next=temp1

            first=temp1
            second=temp2
            