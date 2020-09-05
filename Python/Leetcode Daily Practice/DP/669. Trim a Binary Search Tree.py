class Solution(object):
    def trimBST(self, root, L, R):
        def dfs(root):
            if not root:
                return 

            if root.val < L: #the left side is discarded
                return dfs(root.right)
            if root.val > R: # the right side is discarded 
                return dfs(root.left)
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return root
        return dfs(root)
                