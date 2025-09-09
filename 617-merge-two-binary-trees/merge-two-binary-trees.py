# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(p,q):
            if not p and not q:
                return None
            if not p:
                return q
            if not q:
                return p
            
            root=TreeNode(p.val+q.val)
            root.left=traverse(p.left,q.left)
            root.right=traverse(p.right,q.right)
            return root
        return traverse(root1,root2)