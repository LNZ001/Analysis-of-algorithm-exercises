class Solution:
    def numDecodings(self, s: str) -> int:
        nums = [1]
        length = len(s)
        if length >= 1:
            nums.append(1 if int(s[0]) != 0 else 0)

        if length <= 1:
            return nums[length]

        for i in range(2, length+1):
            v = 0
            if int(s[i - 1]) != 0:
                v += nums[-1]
            if 0 < int(s[i-2:i])<=26 and s[i-2] != "0":
                v += nums[-2]
            nums.append(v)
        return nums[length]


if __name__ == '__main__':
    print(Solution().numDecodings("01"))