from typing import List
import sys
from functools import lru_cache

def gcd(a, b):
    if a == 1 or b == 1: return True
    tmp = a % b
    if tmp == 0:
        return False
    elif tmp == 1:
        return True
    else:
        res = gcd(b, tmp)
    return res

@lru_cache(None)
def get_result(n, k):
    res = [-1]
    if n % k != 0: return [-1]
    v = n // k
    # ######### 将v拆分3个互质的数 ###########
    for i in range(1, v-1):
        left = i + 1
        right = v - 2*i - 1
        while left < right:
            if right < i + 2:
                return res
            if gcd(i, left) and gcd(left, right) and gcd(right, i):
                res = [i*k, left*k, right*k]
                return res
            left += 1
            right -= 1
    return res
'''
3
6 1
12 4
238 2
'''
if __name__ == '__main__':
    length = int(sys.stdin.readline().strip())
    for i in range(length):
        n, k = tuple(map(int, sys.stdin.readline().strip().split(" ")))
        print(" ".join(map(str, get_result(n, k))))
    # print(" ".join(map(str, get_result(15, 16))))