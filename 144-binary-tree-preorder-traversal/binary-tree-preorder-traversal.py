# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if not root:
            return result
        queue=[root]
        while(queue):
            k=queue.pop()
            result.append(k.val)
            if k.right:
                queue.append(k.right)
            if k.left:
                queue.append(k.left)
        return result
