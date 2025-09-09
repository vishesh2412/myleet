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
        
        def traverse(node,level):
            if not node:
                return

            if level==len(answer):
                answer.append([])
            
            traverse(node.left,level+1)
            traverse(node.right,level+1)

            answer[level].append(node.val)


        traverse(root,0)
        return answer