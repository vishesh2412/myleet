# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        fake=ListNode(0)
        temp=head

        while(temp):
            node=temp.next
            prev=fake
            
            while(prev.next and prev.next.val<temp.val):
                prev=prev.next
            
            temp.next=prev.next
            prev.next=temp

            temp=node

        return fake.next