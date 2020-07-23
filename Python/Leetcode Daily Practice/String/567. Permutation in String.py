class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        sliding window 
        """
        from collections import Counter
        total = len(s1)
        cnt = Counter(s1)
        j = 0 
        for i in range(len(s2)):
            cnt[s2[i]]-= 1
            if cnt[s2[i]] >= 0:
                total -= 1
            while total == 0:
                if i - j + 1 == len(s1):
                    return True 
                cnt[s2[j]] += 1
                if cnt[s2[j]]>0:
                    total += 1
                j += 1

        return False 
        



if __name__ == "__main__":

    s1 = "abcdxabcde"
    s2 = "abcdeabcdx"
    # return true 
    print(Solution().checkInclusion(s1, s2))

    # Input: 
    s1 = "ab" 
    s2 = "eidbaooo"
    # Output: True
    # Explanation: s2 contains one permutation of s1 ("ba").
    print(Solution().checkInclusion(s1, s2))
    
    s1 = "ab"
    s2 = "eidboaoo"
    # return False 
    print(Solution().checkInclusion(s1, s2))