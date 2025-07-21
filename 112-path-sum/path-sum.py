class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        #when reaching leaf node
        if not root.left and not root.right:
            if root.val==targetSum:
                return True
            return False

        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)