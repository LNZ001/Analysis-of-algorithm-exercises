import sys
# from collections import Counter

def check(nums):
    res = []
    for num in nums:
        pos_1 = num.index(1)

        if pos_1 == 0:
            pass
        elif pos_1 == 1:
            num[0], num[1] = num[1], num[0]
            num[3], num[2] = num[2], num[3]
        elif pos_1 in [2, 4]:
            num[0], num[pos_1 + 1], num[1], num[pos_1] = num[pos_1], num[0], num[pos_1+1], num[1]
        else:
            num[0], num[pos_1 - 1],  num[1], num[pos_1] = num[pos_1], num[0], num[pos_1 - 1], num[1]

        pos_2 = num.index(2)
        if pos_2 != 1:
            if pos_2 == 2:
                pass
            elif pos_2 == 4:
                num[2], num[3], num[4], num[5] = num[4], num[5], num[3], num[2]
            elif pos_2 == 3:
                # 3
                num[2], num[3], num[4], num[5] = num[3], num[2], num[5], num[4]
            else:
                # 5
                num[2], num[3], num[4], num[5] = num[5], num[4], num[2], num[3]
        else:
            pos_3 = num.index(3)
            if pos_3 == 2:
                pass
            elif pos_3 == 4:
                num[2], num[3], num[4], num[5] = num[4], num[5], num[3], num[2]
            elif pos_3 == 3:
                # 3
                num[2], num[3], num[4], num[5] = num[3], num[2], num[5], num[4]
            else:
                # 5
                num[2], num[3], num[4], num[5] = num[5], num[4], num[2], num[3]

        res.append(tuple(num))

    mapp = {}
    for r in res:
        if mapp.get(r) is None:
            mapp[r] = 1
        else:
            mapp[r] += 1
    # mapp = Counter(res)
    count = 0
    result = []
    for k, v in mapp.items():
        count += 1
        result.append(v)
    result.sort(reverse=True)
    print(count)
    print(" ".join(map(str, result)))
#
# 3
# 1 2 3 4 5 6
# 1 2 6 5 3 4
# 1 2 3 4 6 5

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    nums = []
    for i in range(n):
        nums.append(list(map(int, sys.stdin.readline().strip().split())))
    check(nums)