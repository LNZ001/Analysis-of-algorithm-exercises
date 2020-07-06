from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                e2 = stack.pop()
                e1 = stack.pop()
                stack.append(e1+e2)
            elif t == "-":
                e2 = stack.pop()
                e1 = stack.pop()
                stack.append(e1 - e2)
            elif t == "*":
                e2 = stack.pop()
                e1 = stack.pop()
                stack.append(e1 * e2)
            elif t == "/":
                e2 = stack.pop()
                e1 = stack.pop()
                stack.append(int(e1 / e2))
            else:
                stack.append(int(t))
        return stack.pop()

if __name__ == '__main__':
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))