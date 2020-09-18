"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""

class Solution(object):
    def evalRPN(self, tokens):
        stack_num = []
        stack_ops = []

        for t in tokens:
            if t.isdigit():
                 stack_num.append(int(t))
            else:
                print(t, stack_num)
                num1 = stack_num.pop() if stack_num else 0
                num2 = stack_num.pop() if stack_num else 0
                if t == "+":
                    stack_num.append(num1 + num2)
                elif t == "-":
                    stack_num.append(num2 - num1)
                elif t == "*":
                    stack_num.append(num1 * num2)
                else:
                    stack_num.append(num2//num1)
        return stack_num[-1] if stack_num else -1
tokens= ["2", "1", "+", "3", "*"]
# print(Solution().evalRPN(tokens))


tokens= ["4","13","5","/","+"]
#print(Solution().evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))

