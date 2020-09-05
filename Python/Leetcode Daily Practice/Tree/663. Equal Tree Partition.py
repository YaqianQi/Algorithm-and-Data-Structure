"""
Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:
Input:     
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation: 
    5
   / 
  10
      
Sum: 15

   10
  /  \
 2    3

Sum: 15
Example 2:
Input:     
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
"""
# post-order traversal 
# half-sum 
class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def sum_node(root):
            if not root:
                return 
            cur = root.val + sum_node(root.left) + sum_node(root.right)
            self.map[cur] += 1
            return cur
        from collections import defaultdict
        self.map = defaultdict(int)
        sum_val = sum_node(root)
        if sum_val == 0:
            return self.map[sum_val] > 1
        return sum_val in self.map
         