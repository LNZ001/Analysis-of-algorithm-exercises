from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        if s == "": return True

        length = len(s)

        stack = []
        for i in range(length):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            else:
                if s[i] == ")":
                    if len(stack) > 0 and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif s[i] == "]":
                    if len(stack) > 0 and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    if len(stack) > 0 and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0: return True
        return False

if __name__ == '__main__':
    print(Solution().isValid("(]"))








