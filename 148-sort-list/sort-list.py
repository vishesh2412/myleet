# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        values=[]

        temp=head
        while(temp):
            values.append(temp.val)
            temp=temp.next
        
        values=sorted(values)

        head2=ListNode(0)
        temp=head2

        for i in values:
            new=ListNode(i)
            temp.next=new
            temp=temp.next
        
        return head2.next