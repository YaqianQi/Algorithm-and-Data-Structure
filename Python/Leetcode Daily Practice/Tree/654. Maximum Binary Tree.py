"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # find max, then search left max, search right max..dfs 
        def dfs(start, end):
            if start > end:
                return None
            max_idx = start
            for i in range(start, end + 1):
                if nums[i] > nums[max_idx]:
                    max_idx = i
            cur = TreeNode(nums[max_idx])
            cur.left = dfs(start, max_idx-1)
            cur.right = dfs(max_idx + 1, end)
            return cur 
        return dfs(0, len(nums)-1)

    def constructMaximumBinaryTree2(self, nums):
        q = []
        for num in nums:
            cur = TreeNode(num)
            while q and q[-1].val < num:
                cur.left = q.pop()
            if q:
                q[-1].right = cur
            q.append(cur)
        return q[0] if q else None 

# Input: [3,2,1,6,0,5]
#               i
# node = 1 
# q = [3-> 2, 2->1, 1] 
# 
# 