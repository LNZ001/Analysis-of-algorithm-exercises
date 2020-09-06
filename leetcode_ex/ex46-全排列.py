from typing import List

class Solution:

    def permute(self, nums):
        self.result = []
        n = set(nums)
        self.dfs(n, [])
        return self.result


    def dfs(self, n, res):
        if len(n) == 0:
            self.result.append(res[:])
            return
        for i in list(n):
            res.append(i)
            n.discard(i)
            self.dfs(n, res)
            res.pop()
            n.add(i)



if __name__ == '__main__':
    print(Solution().permute([1,2 ,3 ]))