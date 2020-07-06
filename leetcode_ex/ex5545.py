from tools.time_caculate import count_time
class Solution:

    @count_time
    def minInteger(self, num: str, k: int) -> str:


        n=len(num)
        if k >= n*(n-1)//2:
                return ''.join(sorted(num))
        ans = ''
        while k > 0 and num:
            min_ = num[0]
            target = 0
            for i in range(1, min(k+1,len(num))):
                if num[i] < min_:
                    min_ = num[i]
                    target = i
                num = num[:target] + num[target + 1:]
                k = k - target
                ans = ans + min_
        ans = ans + num
        return ans