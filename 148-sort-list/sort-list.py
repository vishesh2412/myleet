# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        slow,fast=head,head
        prev=None
        while(fast and fast.next):
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None

        left=self.sortList(head)
        right=self.sortList(slow)

        return self.merge(left,right)

    def merge(self,left,right):
        fake=ListNode(0)
        temp=fake

        while(left and right):
            if left.val<=right.val:
                temp.next=left
                left=left.next
            else:
                temp.next=right
                right=right.next
            temp=temp.next
        
        temp.next=left if left else right

        return fake.next
        