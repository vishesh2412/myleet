# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        values=[]
        temp=head
        while temp:
            values.append(temp.val)
            temp=temp.next
        
        stack=[]
        answer=[0]*len(values)

        for i,val in enumerate(values):
            while stack and values[stack[-1]]<val:
                ind=stack.pop()
                answer[ind]=val
            stack.append(i)

        return answer