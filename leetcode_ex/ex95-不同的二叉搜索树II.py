# Definition for a binary tree node.
from typing import List
from functools import lru_cache
import copy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left

class Solution:

    # @lru_cache(None)
    # def dfs(self, start, end):
    #     if start > end: return [None]
    #     result = []
    #     for idx, i in enumerate(range(start, end+1)):
    #         lefts = self.dfs(start, i-1)
    #         rights = self.dfs(i+1, end)
    #         for l in lefts:
    #             for r in rights:
    #                 node = TreeNode(i)
    #                 node.left = l
    #                 node.right = r
    #                 result.append(node)
    #     return result
    #
    # def generateTrees(self, n: int) -> List[TreeNode]:
    #     if n == 0: return []
    #     v = self.dfs(1, n)
    #     return v


    def generateTrees(self, n: int):
        if n == 0:
            return None
        # 对dp进行初始化
        dp = []
        for i in range(0, n + 1):  # 初始化dp
            dp.append([])
            for j in range(0, n + 1):
                if i == j:
                    dp[i].append([TreeNode(i)])
                elif i < j:
                    dp[i].append([])
                else:
                    dp[i].append([None])
        dp[0][0] = [None]
        for i in range(n - 1, 0, -1):  # 自下向上进行循环
            for j in range(i + 1, n + 1):
                for r in range(i, j + 1):  # i-j每一个节点为顶点的情况
                    left = r + 1 if r < j else r  # 右边的值需要边界判断，不然会溢出数组
                    for x in dp[i][r - 1]:  # 左右子树排列组合
                        for y in dp[left][j]:
                            node = TreeNode(r)
                            node.left = x
                            node.right = y
                            if r == j:
                                node.right = None
                            dp[i][j].append(node)  # dp[i][j]添加此次循环的值
        return dp[1][n]

if __name__ == '__main__':
    print(Solution().generateTrees(3))