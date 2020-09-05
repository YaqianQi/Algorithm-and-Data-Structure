class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        preorder 
        """
        def find_min(root):
            min_val = root.val
            while root:
                min_val = root.val 
                root = root.left 
            return min_val
        def dfs(root):
            if not root:
                return 
            if root.val > key:
                dfs(root.left)
            elif root.val < key:
                dfs(root.right)
            else:
                if not root.left:
                    return root.right 
                elif not root.right:
                    return root.left 
                else:
                    min_val = find_min(root.right)
                    root.val = min_val
                    self.deleteNode(root.right, root.val) 
            return root
        return dfs(root)