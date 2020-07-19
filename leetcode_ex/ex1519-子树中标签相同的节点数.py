from typing import List
from collections import defaultdict
# from collections import Counter

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        mapp = defaultdict(list)
        mapp_reverse = defaultdict(list)
        for start, end in edges:
            mapp[start].append(end)
            mapp[end].append(start)


        targets = [0]*n
        def dfs(root, last=None):
            res = defaultdict(int)
            for i in mapp[root]:
                if i == last: continue
                for k, count in dfs(i, last=root).items():
                    res[k] += count
            for i in mapp_reverse[root]:
                if i == last: continue
                for k, count in dfs(i, last=root).items():
                    res[k] += count
            res[labels[root]] += 1
            targets[root] = res[labels[root]]
            return res

        dfs(0)

        return targets

if __name__ == '__main__':
    print(Solution().countSubTrees())


