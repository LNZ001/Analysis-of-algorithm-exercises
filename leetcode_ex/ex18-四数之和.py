from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        if length < 4: return []
        nums.sort()

        res  =[]
        for i in range(length-3):
            if i > 0 and nums[i-1] == nums[i]: continue

            # ########## 这两个小优化直接将 1100ms -> 192ms ##########
            # ########## 优化start ##########
            k=i
            # 获取当前最小值，如果最小值比目标值大，说明后面越来越大的值根本没戏
            min1 = nums[k] + nums[k + 1] + nums[k + 2] + nums[k + 3]
            if min1 > target:
                break
            # 获取当前最大值，如果最大值比目标值小，说明后面越来越小的值根本没戏，忽略
            max1 = nums[k] + nums[length - 1] + nums[length - 2] + nums[length - 3]
            if max1 < target:
                continue
            # ########## 优化end ##########

            for j in range(i+1, length-2):
                if j > i+1 and nums[j-1] == nums[j]: continue

                left = j+1
                right = length-1
                while left <right:
                    v = nums[i] + nums[j] + nums[left] + nums[right]
                    if v == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif v > target:
                        right -= 1
                    else:
                        left += 1

        return res

if __name__ == '__main__':
    print(Solution().fourSum([5,5,3,5,1,-5,1,-2],
4))