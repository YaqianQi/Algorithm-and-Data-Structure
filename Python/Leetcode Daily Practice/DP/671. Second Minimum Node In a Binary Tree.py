class Solution(object):
    def findSecondMinimumValue_bruteforce(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time Complexity: O(N)O(N), where NN is the total number of nodes in the given tree. We visit each node exactly once, and scan through the O(N)O(N) values in unique once.

        # Space Complexity: O(N)O(N), the information stored in uniques.

        self.min_val = root.val
        self.ele_set = {root.val}
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            
            self.ele_set.add(root.val)
            self.min_val = min(self.min_val, root.val)
            dfs(root.right)
            
        dfs(root)
        res = float("inf")
        for x in self.ele_set:
            if x > self.min_val and x < res:
                res = x
        return res if res < float("inf") else -1

    def findSecondMinimumValue(self, root):
        def dfs(root, min_val):
            if not root:
                return -1 
            if root.val > min_val:
                return root.val 
            left = dfs(root.left, min_val)
            right = dfs(root.right, min_val)
            if left == -1 or right == -1:
                return max(left, right)
            else:
                return min(left, right)
        
        if not root:
            return -1
        return dfs(root, root.val)
        