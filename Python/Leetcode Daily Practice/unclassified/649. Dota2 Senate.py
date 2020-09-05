def predictPartyVictory(self, senate):
    from collections import deque
    rq = deque()
    dq = deque()
    n = len(senate)
    for i, s in enumerate(senate):
        if s == "R":
            rq.append(i)
        else:
            dq.append(i)
    while rq and dq:
        r = rq.popleft()
        d = dq.popleft()
        n += 1
        if r < d:
            rq.append(n)
        else:
            dq.append(n)
    return "Radiant" if rq else "Dire"
"""
Input: "RDD"
D: 0, R:1
people = [1,0]
bans = [0,0]
A = [0]
x = 0  

Output: "Dire"
"""