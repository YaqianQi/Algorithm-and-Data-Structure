class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findMode(self, root):
        from collections import defaultdict
        self.d = defaultdict(int)
        def dfs(root):
            if root:
                dfs(root.left)
                self.d[root.val] += 1
                dfs(root.right)
        dfs(root)
        d = list(self.d.items())
        d.sort(key=lambda x: x[1])
        return d[-1][0]
"""
count = collections.Counter()

def dfs(node):
    if node:
        count[node.val] += 1
        dfs(node.left)
        dfs(node.right)
        
dfs(root)
max_ct = max(count.itervalues())
max_ct = max(count.itervalues())
return [k for k, v in count.iteritems() if v == max_ct]
"""

t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(2)
print(Solution().findMode(t))


        