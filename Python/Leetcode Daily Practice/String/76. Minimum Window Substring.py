""" sliding window

s = "A D O B E C O D E B A N C"
               i 

s = "A B C"
'A': 1, 'B': 1, 'C': 1, 'D':-1, 'O': -1
     0       0       0
time o(n)
space o(1)
"""
class Solution(object):
    def minWindow(self, s, t):
        from collections import Counter
        cnt = Counter(t)
        start = 0 
        total = len(t)
        min_val = float("inf")
        j = 0 
        res = ''
        for i in range(len(s)):
            cnt[s[i]] -= 1
            if cnt[s[i]] >= 0:
                total -= 1
            #print(cnt, total)
            while total == 0:
                #print(s[j:i+1])
                if i - j + 1 < min_val:
                    min_val = i - j + 1
                    start = j
                    res = s[j:i+1]
                cnt[s[j]] += 1

                if cnt[s[j]]>0:
                    total += 1
                j+= 1
        if min_val == float("inf"):
            return ""
        return res



if __name__ == "__main__":
    # Input: 
    S = "ADOBECODEBANC"
    T = "ABC"
    # Output: "BANC"
    print(Solution().minWindow(S, T))