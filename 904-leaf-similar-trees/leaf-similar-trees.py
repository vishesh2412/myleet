# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        answer1,answer2=[],[]
        def traverse(root,answer):
            if not root:
                return
            if not root.left and not root.right:
                answer.append(root.val)
            traverse(root.left,answer)
            traverse(root.right,answer)
        
        traverse(root1,answer1)
        traverse(root2,answer2)

        if answer1==answer2:
            return True
        return False