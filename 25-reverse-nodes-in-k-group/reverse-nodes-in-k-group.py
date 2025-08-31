# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node=head
        for _ in range(k):
            if not node:
                return head
            node=node.next

        temp=head
        prev=None
        for _ in range(k):
            new=temp.next
            temp.next=prev
            prev=temp
            temp=new
        
        head.next=self.reverseKGroup(temp,k)
        return prev