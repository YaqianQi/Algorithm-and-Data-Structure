class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        key parent node: value, tree value 
        pid =  [1, 3, 10, 5]
        ppid = [3, 0, 5, 3] 
        kill = 5
        3: [1, 5]
        5: [10]
        """
        res = []
        def dfs(v):
            res.append(v)
            for node in graph[v]:
                dfs(node)
            
        from collections import defaultdict
        graph = defaultdict(list)
        for i in range(len(ppid)):
            graph[ppid[i]].append(pid[i])
        # print(graph)
        res = []
        dfs(kill)
        return res

if __name__ == "__main__":

    pid =  [1, 3, 10, 5]
    ppid = [3, 0, 5, 3] 
    kill = 5
    print(Solution().killProcess(pid, ppid, kill))
"""
Input: 
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3] # parent id # 0 root node 
kill = 5
Output: [5,10]
Explanation: 
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
"""