# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        fake=ListNode(0)
        temp=fake
        
        while True:
            index=-1
            val=float('inf')
            for i in range(len(lists)):
                if lists[i] and lists[i].val<val:
                    val=lists[i].val
                    index=i
                
            if index==-1:
                break

            temp.next=lists[index]
            temp=temp.next
            lists[index]=lists[index].next

        return fake.next