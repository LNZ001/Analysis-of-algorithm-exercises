from typing import List
from collections import defaultdict

class Solution:
    def dp_work(self, isBlue=True):

        if isBlue:
            before = self.result_red
            after = self.result_blue
            edges = self.blue_edges_map
        else:
            before = self.result_blue
            after = self.result_red
            edges = self.red_edges_map

        changed = False
        for start, ends in edges.items():
            if before[start] == -1: continue
            for end in ends:
                last_end = after[end]
                after[end] = before[start]+1 if after[end] == -1 else min(after[end], before[start]+1)
                if last_end != after[end]:
                    changed = True
        if changed:
            self.dp_work(isBlue=not isBlue)

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        if n == 0: return [0]
        self.red_edges_map = defaultdict(list)
        self.blue_edges_map = defaultdict(list)

        for i, j in red_edges:
            self.red_edges_map[i].append(j)
        for i, j in blue_edges:
            self.blue_edges_map[i].append(j)

        self.result_blue = [0] + [-1] * (n-1)
        self.result_red = [0] + [-1] * (n-1)
        # ########## 遍历两次分先红色和先蓝色. ##########
        self.dp_work()
        self.dp_work(False)

        # ########## 合并. ##########
        for idx, r in enumerate(self.result_red):
            if r == -1: continue
            self.result_blue[idx] = r if self.result_blue[idx] == -1 else min(self.result_blue[idx], r)
        return self.result_blue

if __name__ == '__main__':
    print(Solution().shortestAlternatingPaths(5
,[[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]]
,[[1,3],[0,0],[0,3],[4,2],[1,0]]))