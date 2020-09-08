class Solution(object):
    def modifyString(self, s):
        if len(s) == 1 and s[0] == "?":
            return 'a'
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?":
                candidate = [1] * 26
                exclude = []
                if i == 0 :
                    exclude.append(s[i+1])
                elif i == len(s) -1:
                    exclude.append(s[i-1])
                else:
                    exclude.append(s[i-1])
                    exclude.append(s[i+1])
                print(exclude)
                for x in exclude:
                    if x != "?":
                        candidate[ord(x) - ord('a')] -= 1
                for idx, freq in enumerate(candidate):
                    if freq > 0:
                        s[i] = chr(idx + ord('a'))  
                        break
        
        return ''.join(s)
# print(ord("z") - ord('a'))\
print(Solution().modifyString("gm??a?"))
# print(Solution().modifyString("?zs"))

                
                