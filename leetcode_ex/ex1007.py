from typing import List
from collections import defaultdict
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        may_queue = defaultdict(lambda : [0]*2)
        may_v = set()

        for i in range(len(A)):
            if i == 0:
                may_v.add(A[i])
                may_v.add(B[i])
                may_queue[A[i]][0] += 1
                may_queue[B[i]][1] += 1
                continue

            if A[i] in may_v:
                may_queue[A[i]][0] += 1

            if B[i] in may_v:
                may_queue[B[i]][1] += 1

            for j in list(may_v):
                if j not in [A[i], B[i]]:
                    may_v.remove(j)

            if not may_v: return -1

        min_count = float('inf')
        for i in may_v:
            min_count = min(min_count, may_queue[i][0], len(A) - may_queue[i][0], may_queue[i][1], len(A) - may_queue[i][1])


        return min_count

if __name__ == '__main__':
    print(Solution().minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))

