'''
记录区间的算法：(默认去重了。)
left right dict
'''

# class Solution:
#     def longestConsecutive(self, nums):
#         hash_dict = dict()
#
#         max_length = 0
#         for num in nums:
#             if num not in hash_dict:
#                 left = hash_dict.get(num - 1, 0)
#                 right = hash_dict.get(num + 1, 0)
#
#                 cur_length = 1 + left + right
#                 if cur_length > max_length:
#                     max_length = cur_length
#
#                 # hash_dict[num] = cur_length
#                 hash_dict[num - left] = cur_length
#                 hash_dict[num + right] = cur_length
#
#         return max_length

'''
这个是导入set， 然后检查前一个是否为空，不为空就跳过，只检查前一个为空的，这样是一段的最长，并且不会重复。
'''
#
# class Solution:
#     def longestConsecutive(self, nums):
#         longest_streak = 0
#         num_set = set(nums)
#
#         for num in num_set:
#             if num - 1 not in num_set:
#                 current_num = num
#                 current_streak = 1
#
#                 while current_num + 1 in num_set:
#                     current_num += 1
#                     current_streak += 1
#
#                 longest_streak = max(longest_streak, current_streak)
#
#         return longest_streak

'''
并查集的方法：
1. 将x 与x+1结盟（如果x+1存在）
2. 第二轮遍历，计算每一个的find(x)-x+1的大小，找到最大。
（略）
并查集实现和使用. （这种是数据乱序的，还有一种顺序数据，可以简化为使用list存储self.p. 具体见959）

'''
class DSU:
    def __init__(self):
        # 记录第几个的x
        self.p = {}

    def find(self, x):
        parent = self.p.get(x)
        if parent is None: return None
        if parent == x: return x
        self.p[x] = self.find(parent)
        return self.p[x]


    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        dsu = DSU()
        nums = set(nums)
        # 两次遍历， 一次导入数据None，用于第二次时检查x+1是否存在， 一次
        for n in nums:
            dsu.p[n] = n

        # ########## 第二次遍历 ##########
        for n in nums:
            if (n+1) in dsu.p:
                dsu.union(n, n+1)

        return max(dsu.find(sin_p) - sin_p + 1 for sin_p in dsu.p)

if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))