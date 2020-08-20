from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.stack = []
        self.res = []
        self.inner_generateParenthesis(n, 0)
        return self.res


    def inner_generateParenthesis(self, pos, stack_num):
        if pos == 0:
            self.res.append("".join(self.stack) + ")" * stack_num)
            return

        if pos > 0:
            self.stack.append("(")
            self.inner_generateParenthesis(pos-1, stack_num+1)
            self.stack.pop()

        if stack_num > 0:
            self.stack.append(")")
            self.inner_generateParenthesis(pos, stack_num-1)
            self.stack.pop()

        return

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))

