from collections import  Counter
class Solution:
    def minWindow(self, s, t):
        n = len(t)
        j = 0 
        r = 0 
        start = 0 
        min_val = float("inf")
        cnt = Counter(t)
        for i in range(len(s)):
            c = s[i]
            cnt[c] -= 1 
            if cnt[c] >= 0:
                n -= 1
                while n == 0:
                    win_len = i - j + 1
                    if win_len < min_val:
                        min_val = win_len
                        start = j
                    cnt[s[j]] += 1 
                    if cnt[s[j]]> 0:
                        n += 1
                    j+= 1
        if min_val == float("inf"):
            return ""
        return s[start :start + min_val]

# o(n + m)
if __name__ == "__main__":
    # Input: 
    S = "ADOBECODEBANC"
    T = "ABC"
    # Output: "BANC"
    sol = Solution()
    #print(sol.minWindow(S, T))

    S = "a"
    T = "aa"
    # Output: ""
    sol = Solution()
    print(sol.minWindow(S, T))
