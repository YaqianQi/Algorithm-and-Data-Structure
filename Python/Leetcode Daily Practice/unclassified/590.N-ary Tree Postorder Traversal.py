
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root):
        res = []
        def dfs(root):
            if root == None:
                return
            for child in root.children: 
                dfs(child)
            res.append(root.val)
        dfs(root)
        return res
    def postorder2(self, root):
        from collections import deque
        res = []
        if root == None:
            return None 
        stack = deque()
        stack.append(root)
        while stack: 
            cur = stack.pop()
            child = cur.children
            res.insert(0, cur.val)
            for node in child:
                stack.append(node)
        return res
    def postorder_binarytree(self, root):
        from collections import deque
        res = []
        if root == None:
            return None 
        stack = deque()
        stack.append(root)
        while stack: 
            cur = stack.pop()
            res.insert(0, cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res
        