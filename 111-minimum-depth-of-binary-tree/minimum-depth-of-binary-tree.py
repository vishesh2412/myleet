# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if not root:
                return 0
            if root.left and root.right:
                return min(traverse(root.left),traverse(root.right))+1
            elif root.left:
                return traverse(root.left)+1
            else:
                return traverse(root.right)+1
        return traverse(root)