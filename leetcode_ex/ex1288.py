from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        node = [None]*(100000+1)

        for idx, range_v in enumerate(intervals):
            start, end = range_v
            if node[start] == node[end] and node[start] is not None: continue
            for i in range(start, end+1):
                node[i] = idx

        node = set(node)
        # sorted(list, key=lambda x: (x[0], x[1]))
        if None in node: return len(node)-1
        else: return len(node)



if __name__ == '__main__':
    print(Solution().removeCoveredIntervals(intervals = [[1,4],[2, 3]]))