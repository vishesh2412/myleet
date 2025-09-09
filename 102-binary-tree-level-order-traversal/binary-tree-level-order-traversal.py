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
        def traverse(node,l):
            if not node:
                return 
            
            if l==len(a):
                a.append([])

            traverse(node.left,l+1)
            traverse(node.right,l+1)

            a[l].append(node.val)            
            
        traverse(root,0)
        return a