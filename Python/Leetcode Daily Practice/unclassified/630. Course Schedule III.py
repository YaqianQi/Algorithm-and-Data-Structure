"""
(t, d): duration t, end date d 
return max course can take 
Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, 
and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, 
and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, 
which exceeds the closed date.
"""
class Solution(object):
    def scheduleCourse(self, courses):
        # sort based on the last day 
        # then sart based on small duration 
        courses.sort(key=lambda x: x[1])
        print(courses)
        import heapq
        q = []
        time = 0 
        for c in courses:
            time += c[0]
            heapq.heappush(q, -c[0])
            if time > c[1]:
                time -= -heapq.heappop(q)
        return len(q)
arr = [[100, 200], [1000, 1250], [200, 1300], [2000, 3200]]
"""
arr = [[100, 200], [1000, 1250], [200, 1300], [2000, 3200]]
                                               cur
time = 100  + 1000 = 1100 +200 = 1300 
q = [ -1000,-200,-100] 
"""
print(Solution().scheduleCourse(arr))