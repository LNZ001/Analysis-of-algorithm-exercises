'''
要点: 测试了前缀树的写法, 要实例化, 是__getitem__.
可以充分利用字符串比大小的能力.
'''

from typing import List
from functools import reduce
from collections import defaultdict

# class Solution:
#
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         Trie = lambda: defaultdict(Trie)
#         trie = Trie()
#
#         for s in strs:
#             reduce(dict.__getitem__, s, trie)[True] = None
#
#         v = ""
#         cur = trie
#         while True:
#             s = list(cur.keys())
#             if True in s: return v
#             if len(s) == 1:
#                 v += s[0]
#                 cur = cur[s[0]]
#             else:
#                 return v

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))


