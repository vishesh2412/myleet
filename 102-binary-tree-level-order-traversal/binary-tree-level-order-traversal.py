# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        a=[]
        if not root:
            return a
        def traverse(r,l):
            if not r:
                return 
            
            if l==len(a):
                a.append([])

            traverse(r.left,l+1)
            traverse(r.right,l+1)

            a[l].append(r.val)            
            
        traverse(root,0)
        return a