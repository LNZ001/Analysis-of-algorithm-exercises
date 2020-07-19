from typing import List

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        count = 0
        for i in range(len(A)):
            if i == 0 or A[i] > A[i-1]: continue
            count += A[i-1] + 1 - A[i]
            A[i] = A[i-1] + 1
        return count

if __name__ == '__main__':
    print(Solution().minIncrementForUnique([3,2,1,2,1,7]))
