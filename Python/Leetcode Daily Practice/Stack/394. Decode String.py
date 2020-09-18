class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str

        Input: s = "3[a]2[bc]"
        Output: "aaabcbc"
        [: push in 
        ]: pop out
        digital 
        character 
        """
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString

s = "3[a]2[bc]"
print(Solution().decodeString(s))