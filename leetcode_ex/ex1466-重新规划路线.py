from typing import List
from collections import defaultdict
from functools import lru_cache

class Solution:

    count = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        mapp = defaultdict(list)
        mapp_re= defaultdict(list)
        for start, end in connections:
            mapp[start].append(end)
            mapp_re[end].append(start)

        def dfs(n, last_n=None):
            for end in mapp.get(n, []):
                if (last_n != end or last_n is None):
                    self.count += 1
                    dfs(end, n)

            for start in mapp_re.get(n, []):
                if(last_n != start or last_n is None):
                    dfs(start, n)
        dfs(0)
        return self.count

if __name__ == '__main__':
    print(Solution().minReorder())
