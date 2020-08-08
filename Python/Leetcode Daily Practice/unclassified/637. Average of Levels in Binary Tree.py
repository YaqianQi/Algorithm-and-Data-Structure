class Solution(object):
    def averageOfLevels(self, root):
        # bfs 
        from collections import deque
        res = []
        if not root:
            return res  
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            sum_val = 0 
            for i in range(size):
                cur = q.popleft()
                sum_val += cur.val 
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(sum_val /size)
        return res
"""
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, 
and on level 2 is 11. 
Hence return [3, 14.5, 11].
"""