
class Solution(object):
    def scoreOfParentheses2(self, S):
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
            print(stack)
        return stack.pop()

    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        res = 0 
        t =0 
        for s in S:
            if s == "(":
                stack.append(")")
            else:
                if stack and stack[-1] == s:
                    stack.pop()
                    stack.append(1)
                elif stack and stack[-1]!= s:
                    t = 0
                    while stack[-1]!= ")" :
                        t += stack.pop()
                    if stack[-1] == ")":
                        stack.pop()
                        t *=2
                        stack.append(t)
        while stack:
            res += stack.pop()
        return res
                    
                


if __name__ == "__main__":
    # Input: 
    s = "()"
    #Output: 1
    sol = Solution()
    print(sol.scoreOfParentheses(s))
    
    # Input: 
    s = "(())"  
    # (1)
    # Output: 2
    sol = Solution()
    print(sol.scoreOfParentheses(s))

    # Input: 
    s = "()()"
    # Output: 2
    sol = Solution()
    print(sol.scoreOfParentheses(s))

    # Input: 
    s = "(()(()))" # (1 + 2) * 2 stack = (1
    # Output: 6
    sol = Solution()
    print(sol.scoreOfParentheses2(s))

    
