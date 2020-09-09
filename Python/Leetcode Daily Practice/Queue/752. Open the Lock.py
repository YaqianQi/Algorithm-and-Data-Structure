class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(key):
            lst = []
            for i in range(4):
                x = int(key[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    val = key[:i] + str(y) + key[i+1:] 
                    lst.append(val)
            return lst

        from collections import deque 
        q = deque()
        q.append(["0000", 0])
        visited = set()

        while q:
            cur, cnt = q.popleft()
            if cur == target:
                return cnt
            if cur in deadends:
                continue
            for next_key in neighbors(cur):
                if next_key not in visited:
                    visited.add(next_key)
                    q.append([next_key, cnt + 1])
        return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(Solution().openLock(deadends, target))