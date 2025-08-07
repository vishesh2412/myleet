# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head=None
        
        while(list1 or list2):
            if not list1:
                temp.next=list2
                break
            if not list2:
                temp.next=list1
                break

            if (list1.val<=list2.val):
                new=ListNode(list1.val)
                list1=list1.next
            else:
                new=ListNode(list2.val)
                list2=list2.next
            
            if not head:
                head=new
                temp=head
            else:
                temp.next=new
                temp=temp.next
        return head       