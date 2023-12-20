class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        stack = deque()
        for token in tokens:
            # print(stack)
            if token == "-":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp2-temp1)
            elif token == "+":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp2+temp1)
            elif token == "/":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(int(temp2*(1/temp1)))
            elif token == "*":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp2*temp1)
            else:
                stack.append(int(token))
            
        return stack.pop()