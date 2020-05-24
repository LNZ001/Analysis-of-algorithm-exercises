class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cur = 0
        res = 0
        for idx, key in enumerate(s):
            cur += key in "aeiou"
            if 0 <= idx-k:
                cur -= s[idx-k] in "aeiou"

            res = max(res, cur)
        return res

if __name__ == '__main__':
    print(Solution().maxVowels("thiiitest", 3))