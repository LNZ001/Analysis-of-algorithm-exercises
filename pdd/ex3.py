import sys
def check(n, m, t, ns, ms):
    if t == 0: return 0
    ns.sort(key=lambda x: x[0])
    ms.sort(key=lambda x: x[0])

    last_n = None
    i = 0
    while i < n:
        if last_n is None:
            last_n = ns[i]
            i += 1
            continue
        if last_n is not None and ns[i][1] <= last_n:
            ns.pop(i)
        else:
            last_n = ns[i]
            i += 1

    i = 0
    while i < n:
        if last_n is None:
            last_n = ns[i]
            i += 1
            continue
        if last_n is not None and ns[i][1] <= last_n:
            ns.pop(i)
        else:
            last_n = ns[i]
            i += 1

    n = len(ns)
    m = len(ms)
    if n > 0 and m > 0 and ns[-1][1] + ms[-1][1] < t: return -1
    if n == 0 and m == 0 and t > 0: return -1
    if n == 0 and ms[-1][1] < t: return -1
    if m == 0 and ns[-1][1] < t: return -1
    great = float("inf")
    for i in range(n):
        if ns[i][1] >= t:
            great = min(great, ns[i][0])
    for i in range(m):
        if ms[i][1] >= t:
            great = min(great, ms[i][0])


    if m > 0 and n > 0:
        left = 0
        right = m-1
        while left < n and right >= 0:
            v = ns[left][1] + ms[right][1]
            if v == t:
                great = min(great, ns[left][0] + ms[right][0])
                left += 1
                right -= 1
            elif v < t:
                left += 1
            elif v > t:
                great = min(great, ns[left][0] + ms[right][0])
                right -= 1
    if great == float("inf"): return -1
    return great

if __name__ == '__main__':
    n, m, t = list(map(int, sys.stdin.readline().strip().split()))
    ns, ms = [], []
    for i in range(n):
        ns.append(tuple(map(int, sys.stdin.readline().strip().split())))
    for i in range(m):
        ms.append(tuple(map(int, sys.stdin.readline().strip().split())))
    print(check(n, m, t, ns, ms))