class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ""
        max_length = 0
        max_left = None
        max_right = None
        for i in range(len(s)):
            left = i
            right = i
            while left-1>=0 and right+1 <= len(s)-1:
                if s[left-1] != s[right+1]: break
                left -= 1
                right += 1
            if right-left+1 > max_length:
                max_length = right-left+1
                max_left = left
                max_right = right

            if i+1 <= len(s)-1 and s[i] == s[i+1]:
                left = i
                right = i+1
                while left - 1 >= 0 and right + 1 <= len(s) - 1:
                    if s[left - 1] != s[right + 1]: break
                    left -= 1
                    right += 1
                if right - left + 1 > max_length:
                    max_length = right - left + 1
                    max_left = left
                    max_right = right

        return s[max_left:max_right+1]

if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))


