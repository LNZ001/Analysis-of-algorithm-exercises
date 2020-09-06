from typing import List

class Solution:

    def work(self, n, m, tang):
        '''

        :param n: 行数
        :param m: 列数
        :param tang: 输入的n*m矩阵数组
        :return:
        '''
        self.n = n
        self.m = m
        self.tang = tang
        self.mapp = {}
        self.region = []

        # 计算总共1的个数
        sum_one = sum([sum(i) for i in self.tang])

        for i in range(n*m):
            self.check(i)

        max_v = 0
        for i in range(n*m):
            r = i // self.m
            c = i % self.m
            cur_sum = set()
            for rp, cp in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= rp < self.m and 0 <= cp < self.n:
                    j = rp*self.m + cp
                    v = self.mapp.get(j)
                    if v is not None:
                        cur_sum.add(v)

            cur_sum_v = sum(self.region[d] for d in cur_sum)
            max_v = max(max_v, cur_sum_v)

        return min(sum_one, max_v+1)

    def check(self, k):
        r = k // self.m
        c = k % self.m
        # 如果为1
        if self.tang[r][c] == 1:
            self.tang[r][c] = 0
            self.region.append(1)
            self.mapp[k] = len(self.region)-1
            self.dfs(k)


    def dfs(self, k):
        r = k // self.m
        c = k % self.m
        if r-1>=0 and self.tang[r-1][c] == 1:
            self.tang[r-1][c] = 0
            tmp = (r-1)*self.m+c
            self.region[-1] += 1
            self.mapp[tmp] = len(self.region) - 1
            self.dfs(tmp)

        if r+1<self.n and self.tang[r+1][c] == 1:
            tmp = (r+1)*self.m+c
            self.tang[r+1][c] = 0
            self.region[-1] += 1
            self.mapp[tmp] = len(self.region) - 1
            self.dfs(tmp)

        if c-1 >= 0 and self.tang[r][c-1] == 1:
            self.tang[r][c-1] = 0
            tmp = r*self.m + (c-1)
            self.region[-1] += 1
            self.mapp[tmp] = len(self.region) - 1
            self.dfs(tmp)

        if c+1 < self.m and self.tang[r][c+1] == 1:
            self.tang[r][c+1] = 0
            tmp = r*self.m + (c+1)
            self.region[-1] += 1
            self.mapp[tmp] = len(self.region) - 1
            self.dfs(tmp)

if __name__ == '__main__':
    import sys
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    tang = []
    for i in range(n):
        tang.append(list(map(int, sys.stdin.readline().strip().split())))

    print(Solution().work(n, m, tang))