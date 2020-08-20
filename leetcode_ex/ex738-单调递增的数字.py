class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        nums = list(map(int, str(N)))
        res = "0"
        cur = 0
        while cur < len(nums):
            if cur+1 == len(nums) or int(str(nums[cur]) * (len(nums)-cur)) <= int(str(N)[cur:]):
                res += str(nums[cur])
                cur += 1
                continue
            else:
                res += str(nums[cur]-1) + "9"* (len(nums) - cur - 1)
                break

        return int(res)

if __name__ == '__main__':
    print(Solution().monotoneIncreasingDigits(1234))