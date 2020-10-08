"""
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from collections import deque
        q = []
        q.append((root, 0))
        while q:
            q_size = len(q)
            t = []
            # print(q)
            for i in range(q_size):
                cur, idx = q.pop(0)
                if idx % 2 == 0: # even idx, increasing odd value 
                    if (t and cur.val <= t[-1]) or cur.val % 2 != 1:
                        return False
                else:# odd, desc 
                    if (t and cur.val >= t[-1]) or cur.val % 2 != 0:
                        return False
                t.append(cur.val)
                if cur.left:
                    q.append((cur.left, idx + 1))
                if cur.right:
                    q.append((cur.right, idx + 1))
        return True
t = TreeNode(5)
t.left = TreeNode(9)
t.right = TreeNode(1)
t.left.left = TreeNode(3)
t.left.right = TreeNode(5)
t.right.left = TreeNode(7)

print(Solution().isEvenOddTree(t))
