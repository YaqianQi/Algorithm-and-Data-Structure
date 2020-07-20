
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        courses = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
        graph = [[1, 7],  1
                [],       2 
                [],       3
                [],       4
                [6],      5
                [0],      6
                [2],      7
                [1]]      8
        # return true  
        """
        def dfs(v, graph, visited):
            # visiting: 1, visited: 2 
            # return True: cycle, False: No cycle
            if visited[v] == 1:
                return True
            if visited[v] == 2:
                return False 
            visited[v] = 1
            for neighbor in graph[v]:
                if dfs(neighbor, graph,visited):
                    return True
            visited[v] = 2
            return False
        
        visited = [0] * numCourses
        graph = [[] for i in range(numCourses)]
        for c in prerequisites:
            cur_course = c[1]
            pre_course = c[0]
            graph[cur_course].append(pre_course)
        for i in range(numCourses):          
            if dfs(i, graph,visited):
                return False
        print(graph)
        return True



if __name__ == "__main__":
    #[cur_course, prerequisite]
    courses = [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0]]
    courses = [[1,0],[0,1]]
    # return False 
    #sol = Solution()
    #print(sol.canFinish(2,courses))
    courses = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
    # return true  
    sol = Solution()
    print(sol.canFinish(8,courses))