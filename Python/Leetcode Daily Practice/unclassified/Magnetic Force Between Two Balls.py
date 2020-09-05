"""
Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. 
The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.


Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
"""

class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        def helper(dist, start):
            cnt = 2
            pos = start + 1 
            for i in range(len(position[1:])):
                if position[i] == pos:
                    cnt += 1
                    pos += dist
            return cnt

        left = min(position)
        start = min(position)
        right = max(position)
        dist = 0 
        # 6, 0, 3 
        while left <= right:
            dist = int((right - left) / (m - 2 + 1))
            cnt = helper(dist, start)
            #print(dist, cnt)
            if cnt >= m: # dist bigger  
                return dist
            #elif cnt > m: # dist bigger
             #   left = dist + 1
             #   break
            else:
                right = dist - 1 # dist smaller 
             
        return dist
        
        
position = [1,2,3,4,7]
m = 3
print(Solution().maxDistance(position, m))
    
position = [5,4,3,2,1,1000000000]
m = 2
print(Solution().maxDistance(position, m))
