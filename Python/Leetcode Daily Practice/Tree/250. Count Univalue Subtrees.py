"""\Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.
"""
class Solution(object):
    def countUnivalSubtrees(self, root):
        res = 0 
        def dfs(root):
            if not root:
                return True 
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                if root.left and root.val != root.left.val:
                    return False 
                if root.right and root.val != root.right.val:
                    return False 
                res += 1
                return True 
            return False
        dfs(root)
        return res