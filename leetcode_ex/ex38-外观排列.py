from typing import List

class Solution:

    def countAndSay(self, n: int) -> str:

        return self.dfs(n, "1")

    def dfs(self, n, s):
        if n == 1: return s
        pos = 0
        pre = None
        count = 0

        res = []
        while pos < len(s):
            if pre is None:
                pre = s[pos]
                count = 1
                pos += 1
                continue

            while pos < len(s) and s[pos] == pre:
                count += 1
                pos += 1

            res.append(count)
            res.append(pre)
            if pos < len(s):
                pre = s[pos]
                count = 1
                pos += 1
            else:
                count = 0

        if count != 0:
            res.append(count)
            res.append(pre)

        return self.dfs(n-1, "".join(map(str, res)))

if __name__ == '__main__':
    print(Solution().countAndSay(4))