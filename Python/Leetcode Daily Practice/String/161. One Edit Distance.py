class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        1. abcre abere
        2. abdc abc 
        3. abc abdc
        
        a c b
        a b
          i 
        """
        ns, nt = len(s), len(t)
        min_len = min(len(s), len(t))
        if len(s) < len(t):
            s,t = t, s
        for i in range(min_len):
            if s[i] != t[i]:
                if len(t) == len(s):
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]

        return abs(ns - nt) == 1

if __name__ == "__main__":
    s = "ab"
    t = "acb"
    print(Solution().isOneEditDistance(s, t))