"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

class Solution(object):
    def hasPathSum(self, root, sum):
        def dfs(root, sum_val):
            
            
            if sum_val == root.val and not root.left and not root.right:
                return True 
            if not root:
                return False
            left = dfs(root.left, sum_val - root.val)
            right = dfs(root.right, sum_val - root.val)
            return left or right 
        return dfs(root, sum)
        