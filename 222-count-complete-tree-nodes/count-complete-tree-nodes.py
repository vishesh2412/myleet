# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        def cal(root):
            if not root:
                return 0
            return 1+cal(root.left)+cal(root.right)
        return cal(root)
        