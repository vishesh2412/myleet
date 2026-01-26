# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if(head==None or head.next==None):
            return head
        value=head.val
        temp=head.next
        prev=head
        while(temp!=None):
            if temp.val==value:
                prev.next=temp.next
                temp=temp.next
            else:
                value=temp.val
                prev=temp
                temp=temp.next
        return head