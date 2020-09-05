class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # find the first ascending digits and swap them 
        # if no ascending digits, return original value 
        # break when 238 
        # bucket sort is right solution. 
        s = list(str(num))
        buckets = [0] * 10
        for i in range(len(s)):
            buckets[int(s[i])] = i

        for i in range(len(s)):
            for j in range(9, int(s[i]), -1):
                if buckets[j]>i:
                    s[i], s[buckets[j]] = s[buckets[j]], s[i]
                    return int(''.join(s))
        return num
print(Solution().maximumSwap(2736))