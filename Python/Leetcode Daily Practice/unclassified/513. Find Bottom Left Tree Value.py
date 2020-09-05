class Solution(object):
    def findBottomLeftValue(self, root):
        self.next_max_level = 0 
        self.bot_left_val = 0 
        def dfs(root, level):
            if not root:
                return 
            
            if level == next_max_level:
                self.bot_left_val = root.val 
                self.next_max_level += 1
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return self.bot_left_val
    def findBottomLeftValue(self, root):
        from collections import deque 
        q = [root]
        next_layer = []
        while q:
            for node in q:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            if not next_layer:
                return cur_layer[0].val            
            q = next_layer
            next_layer = []

        