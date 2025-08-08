# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output=[]
        if not root:
            return output

        def traverse(answer,node):
            if not node:
                return ''
            if not node.left and not node.right:
                output.append(answer+str(node.val))
            l=traverse(answer+str(node.val)+'->',node.left)
            r=traverse(answer+str(node.val)+'->',node.right)

        traverse('',root)       
        return output