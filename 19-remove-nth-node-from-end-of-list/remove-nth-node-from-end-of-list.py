# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=ListNode(0,head)
        first=temp
        second=temp

        for _ in range(n+1):
            if not first:
                return head
            first=first.next

        while first:
            first=first.next
            second=second.next
        
        second.next=second.next.next

        return temp.next