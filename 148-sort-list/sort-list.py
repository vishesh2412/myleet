# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        values=[]
        while(head):
            values.append(head.val)
            head=head.next
        
        values.sort()

        head2=ListNode(0)
        temp=head2

        for i in values:
            temp.next=ListNode(i)
            temp=temp.next
        
        return head2.next