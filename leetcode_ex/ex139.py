from typing import List
from functools import reduce
import collections

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = collections.Counter(wordDict)
        dp = [True]

        for i in range(1, len(s) + 1):
            dp.append(reduce(lambda x, y: x | y, [dp[k] and s[k:i] in wordDict for k in range(i)]))

        return dp[len(s)]

if __name__ == '__main__':
    s = "catsandog"
    wordDict = ["cats","og", "sand","and", "cat"]
    print(Solution().wordBreak(s, wordDict))