# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

if __name__ == "__main__":
    # check wether the tree is complete subtree of given tree 
    t = TreeNode(3)
    t.left = TreeNode(4)
    t.right = TreeNode(5)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(2)


    s = TreeNode(4)
    s.left = TreeNode(1)
    s.right = TreeNode(2)

    print(Solution().isSubtree(t, s))