class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def __init__(self):
        from collections import defaultdict
        self.visited = defaultdict(Node)
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]
        
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node
            
                


# Input: 
adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: 
[[2,4],[1,3],[2,4],[1,3]]