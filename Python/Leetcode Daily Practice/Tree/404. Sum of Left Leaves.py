class Solution(object):
    # iterative 
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
        """
        def dfs(root):
            if not root:
                return 0
            res = 0 
            if root.left:
                if not root.left.left and not root.left.right:
                    res += root.left.val
                else:
                    res += dfs(root.left)
            res += dfs(root.right)
            return res
        return dfs(root)

    def sumOfLeftLeaves_bfs(self, root):
        from collections import deque 
        q = deque()
        q.append(root)
        res = 0
        if not root:
            return 0 
        while q:
            cur = q.popleft()
            if cur and cur.left:
                if not cur.left.left and not cur.left.right:
                    res += cur.left.val 
                else:
                    q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res
    # recursive dfs        
    def sumOfLeftLeaves_recursive(self, root):
        def dfs(root, is_left):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if is_left else 0
            return dfs(root.left, True) + dfs(root.right, False) 
        
        return dfs(root, False)