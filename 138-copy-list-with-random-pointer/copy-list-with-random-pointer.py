"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
            
        nodes={}
        temp=head

        while temp:
            nodes[temp]=Node(temp.val)
            temp=temp.next
        
        temp=head
        while temp:
            if temp.next:
                nodes[temp].next=nodes[temp.next]
            if temp.random:
                nodes[temp].random=nodes[temp.random]
            temp=temp.next
        
        return nodes[head]