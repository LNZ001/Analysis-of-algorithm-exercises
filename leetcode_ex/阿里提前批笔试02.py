import sys
from functools import lru_cache


@lru_cache(None)
def dfs(n):
    if n == 7: return True
    if n < 10: return False
    cur = n
    last_v = None
    num = []
    while cur != 0:
        v = cur % 10
        cur = cur // 10
        if last_v is not None:
            num.append(abs(v-last_v))
        last_v = v

    new_v = 0
    for n in num[::-1]:
        new_v = new_v * 10 + n

    return dfs(new_v)


@lru_cache(None)
def get_result(n, k):
    return sum(dfs(i) for i in range(n, k+1))

if __name__ == '__main__':
    length = int(sys.stdin.readline().strip())
    for i in range(length):
        n, k = tuple(map(int, sys.stdin.readline().strip().split(" ")))
        print(get_result(n, k))
