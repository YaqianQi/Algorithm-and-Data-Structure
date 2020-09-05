class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        round_len = n
        from collections import  defaultdict
        n = len(rounds)
        d = defaultdict(int)
        for i in range(1, n):
            prev = rounds[i-1]
            cur = rounds[i]
            if prev > cur:
                while prev <= round_len:
                    d[prev] += 1
                    prev += 1
                prev = 1

            while prev < cur:
                d[prev] += 1
                prev += 1
        d[rounds[-1]]+=1
        max_val = max(d.values())
        return [key for key, val in d.items() if val == max_val]

print(Solution().mostVisited(n=4, rounds=[1,3,2]))
""" 
Input: n = 4, rounds = [1, 3, 1, 2]
                        s
                                cur
[1:2, 2:1, 3: 1, 4: 1]  
1 -> 2->3 ->4->1 ->2
Output: [1,2]
Explanation: The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. 
Sectors 3 and 4 are visited only once.
"""
