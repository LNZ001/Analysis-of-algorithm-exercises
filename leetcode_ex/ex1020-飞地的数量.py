from typing import List

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if len(A) == 1: return 0
        if len(A[0]) == 1: return 0
        # ########## 陆地总数 ##########
        all = sum(sum(A[i]) for i in  range(len(A)))

        count_x = len(A[0])
        count_y = len(A)

        count = 0
        queue = []
        for i in range(0, count_x):
            for j in [0, count_y-1]:
                if A[j][i] == 1:
                    queue.append((j, i))
                    A[j][i] = -1
                    count += 1

        for j in range(0, count_y):
            for i in [0, count_x-1]:
                if A[j][i] == 1:
                    queue.append((j, i))
                    A[j][i] = -1
                    count += 1

        while queue:
            x, y = queue.pop()

            def check(a, b):
                if 0 <= a < count_y and 0 <= b < count_x and A[a][b] == 1:
                    queue.append((a, b))
                    A[a][b] = -1
                    return True
                return False

            if check(x, y+1): count += 1
            if check(x, y-1): count += 1
            if check(x+1, y): count += 1
            if check(x-1, y): count += 1

        return all - count

if __name__ == '__main__':
    print(Solution().numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))


