class Solution:


    def minCut(self, s: str) -> int:

        # def isPalindrome(s):
        #     left, right = 0,len(s)-1
        #     while left < right:
        #         if s[left] == s[right]:
        #             left+=1
        #             right-=1
        #         else:
        #             return False
        #     return True

        isPalindrome = lambda s: s[::-1] == s
        dp = [-1, 0]
        for i in range(1, len(s)):
            dp.append(min([dp[-1]]+[dp[j] for j in range(i) if isPalindrome(s[j: i+1])])+1)
        return dp[-1]

if __name__ == '__main__':
    print(Solution().minCut("aaaaaaaaaaaaa"))