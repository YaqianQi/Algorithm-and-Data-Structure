class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        # back tracking 
        """
        self.res = []
        def dfs(root, sum_val, t):
            if sum_val == 0:
                self.res.append(t)
                return 
            if root.val < sum_val:
                dfs(root.left, sum_val - root.val)
                dfs(root.right, sum_val - root.val)
        dfs(root, sum, [])
        return self.res


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(root, sum_val, t):
            if not root:
                return 
        
            if sum_val == root.val and not root.right and not root.left:
                t = t+[root.val]
                self.res.append(list(t))
            else:
                dfs(root.left, sum_val - root.val, t+[root.val])
                dfs(root.right, sum_val - root.val, t+[root.val])
        dfs(root, sum, [])
        return self.res
             
            