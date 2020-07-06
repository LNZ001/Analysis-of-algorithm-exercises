from typing import List
from functools import reduce
import collections

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = collections.Counter(wordDict)
        dp = [[""]]

        queue = []
        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and (s[k:i] in wordDict):
                    queue.extend({f"{q}{' ' if q != '' else ''}{s[k:i]}" for q in dp[k]})
            dp.append(queue)
            queue = []

        return dp[len(s)]
#
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         tmp = set("".join(wordDict))
#         if any([i not in tmp for i in s]):
#             return []
#         dp = [[""], [s[0]]*(s[0] in wordDict)]
#         for i in range(1, len(s)):
#             dp.append(sum([[f"{k} {s[j: i+1]}" if k else s[j: i+1] for k in dp[j]] for j in range(i+1) if s[j: i+1] in wordDict and dp[j]], []))
#         return dp[-1]

from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        @lru_cache(None)
        def back_track(word):
            if not word:
                return [""]

            queue = []
            for i in range(0, len(word)):
                if word[i:] in wordDict:
                    res = back_track(word[:i])
                    if res:
                        queue.extend({f"{q}{' ' if q != '' else ''}{word[i:]}" for q in res})

            return queue

        return back_track(s)

if __name__ == '__main__':
    s = "pineapplepenapple"
    wordDict = ["apple","pen", "applepen","pine", "pineapple"]
    print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))