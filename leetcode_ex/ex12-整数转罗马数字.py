class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        stacks = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        # ########## 1000 ##########
        for i in range(len(nums)):
            v = num//nums[i]
            res += stacks[i]*v
            num -= v*nums[i]

        return res

if __name__ == '__main__':
    print(Solution().intToRoman(1994))

