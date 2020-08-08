class Solution(object):
    def exclusiveTime(self, n, logs):
        res = [0] * n
        from collections import deque 
        stack = deque()
        for idx, log in enumerate(logs):
            log_vals = log.split(":")
            thread = int(log_vals[0])
            func = log_vals[1]
            time = int(log_vals[2])
            if func == "start":
                stack.append((thread, time))
            else:
                run_time = time - stack.pop()[1]+1
                res[thread] += run_time
                if stack:
                    res[stack[-1][0]]-= run_time
        return res
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print(Solution().exclusiveTime(n, logs))