
import sys

def check(k, n, nums):
    if k == 0: return "paradox"
    re_count = 0
    for i, num in enumerate(nums):
        if k < num:
            re_count += 1
        k = abs(k - num)
        if k == 0:
            if i < n-1:
                return "paradox"
            else:
                return str(0) + " " + str(re_count)
    return str(k) + " " + str(re_count)

if __name__ == '__main__':
    k, n  = list(map(int, sys.stdin.readline().strip().split()))
    nums = list(map(int, sys.stdin.readline().strip().split()))
    print(check(k, n, nums))