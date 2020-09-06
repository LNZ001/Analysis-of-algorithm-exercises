

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0: return ''
        dp = [0]*length
        dp[0] = 1


        for i in range(1, length):
            if i == 1:
                if s[i-1] == s[i]:
                    dp[i] = 2
                else:
                    dp[i] = 1
            else:
                pre = i-1 - dp[i-1]
                if pre >= 0 and s[i] == s[pre]:
                    dp[i] = dp[i-1] + 2
                else:
                    if s[i-1] == s[i]:
                        v = set(s[i+1-dp[i-1]: i+1])
                        if len(v) == 1:
                            dp[i] = dp[i-1]+1
                            continue
                    dp[i] = 1

        pal = 0
        for i in range(length):
            if i - dp[i] + 1 == 0:
                pal = max(pal, dp[i])

        v = s[pal:]


        return v[::-1]+s

if __name__ == '__main__':
    print(Solution().shortestPalindrome("abababababfe"))