



import sys
count = 0

def work(key, nums):
    global count
    count += 1
    # 3. python3.4不支持， 并且赛马不会返回异常，而是捕捉，返回什么都没有。
    # print(f"第{count}批数据.")
    print(count)
    print(key)
    print(nums)

'''
3 1
2 3 1
5 4
1 2 1
3 4 0
2 5 1
3 2 1
'''

if __name__ == '__main__':
    key = None
    nums = []

    ins = sys.stdin.readlines()
    for r in ins:
        res = list(map(int, r.strip().split(" ")))
        # ########## 1. 满足的起始行长度条件 ##########
        if len(res) == 2:
            if key is not None:
                work(key, nums)
            # ########## 2. 关键的key设置, 这两个都是按照上面数据作为测试用例编写的。 ##########
            key = res[1]
            nums = []
        else:
            nums.append(res)

    if key is not None:
        work(key, nums)



# if __name__ == '__main__':
#     res = None
#     while True:
#         try:
#             res = input()
#             ...
#         except:
#             break
