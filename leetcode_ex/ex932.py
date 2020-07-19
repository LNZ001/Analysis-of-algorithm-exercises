from typing import List

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        memo = {1: [1]}

        def f(N):
            if (N not in memo):
                odds = f((N+1)//2)
                evens = f(N//2)
                memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[N]
        return f(N)

if __name__ == '__main__':
    print(Solution().beautifulArray(5))