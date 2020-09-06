class Solutoin:

    def twosplitLeft(self, nums, target):
        '''
        找左边界, 没有会返回第一个大于的数的位置(可以达到长度)
        :param nums:
        :param target:
        :return:
        '''
        l = 0
        r = len(nums)-1
        mid = l + (r-l)//2
        while l <= r:
            if nums[mid] == target:
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            mid = l + (r-l)//2

        # if l < len(nums) and nums[l] == target:
        #     return l
        # return -1
        return l


    def twosplitRight(self, nums, target):
        '''
        找右边界, 没有会返回最近一个左侧小于的数的位置(可以达到-1)
        :param nums:
        :param target:
        :return:
        '''
        l = 0
        r = len(nums)-1
        mid = l + (r-l)//2
        while l <= r:
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            mid = l + (r-l)//2

        # if r >= 0 and nums[r] == target:
        #     return r
        # return -1
        return r

if __name__ == '__main__':
    nums = [1, 2, 3, 3, 5, 6, 7]
    target = 10
    print(Solutoin().twosplitLeft(nums, target))
    print(Solutoin().twosplitRight(nums, target))