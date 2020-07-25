# dictionary counter 
# start from the largest one 
# if no value, next 
# if next value is current value, idle 
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        from heapq import heappush, heappop
        d = defaultdict(int)
        for t in tasks:
            d[t] += 1
        
        h = []
        for key, val in d.items():
            heappush(h, -val)

        res = 0 
        while h:
            t = []
            i = 0
            while i <= n:
                if h:
                    if -h[0]>1:
                        t.append(heappop(h)+1)
                    else:
                        heappop(h)
                res += 1
                if not t and not h:
                    break
                i+= 1
            for x in t:
                heappush(h, x)
        return res

if __name__ == "__main__":
    # Input: 
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(Solution().leastInterval(tasks,n))
    # Output: 8
    # Explanation: 
    # A -> B -> idle -> A -> B -> idle -> A -> B
    # There is at least 2 units of time between any two same tasks.