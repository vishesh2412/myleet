# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer=[]
        if not root:
            return answer
        queue=[root]
        while(queue):
            answer.append([i.val for i in queue])
            new=[]
            for i in queue:
                if i.left:
                    new.append(i.left)
                if i.right:
                    new.append(i.right)
            queue=new
        return answer