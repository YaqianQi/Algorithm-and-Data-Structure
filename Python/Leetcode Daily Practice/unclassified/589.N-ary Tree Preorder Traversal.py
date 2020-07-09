class Solution:
    def preorder(self, root):
        res = []
        def dfs(root):
            if root == None:
                return 
            res.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return res
    
    def preorder2(self, root):
        res = []
        if root is None:
            return res
      
        stack = [root, ]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children[::-1])
         
        return res