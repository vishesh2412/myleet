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
        def traverse(node,level):
            if not node:
                return 
            
            if level==len(a):
                a.append([])

            traverse(node.left,level+1)
            traverse(node.right,level+1)

            a[level].append(node.val)            
            
        traverse(root,0)
        return a