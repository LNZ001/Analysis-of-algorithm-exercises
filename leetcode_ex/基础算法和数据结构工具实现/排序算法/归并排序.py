'''
实现递归和非递归两种.
'''

# 从上而下的递归版
class Solution:

    def merge(self, s1, s2, s):
        i = j = 0
        while i+j < len(s):
            if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
                s[i+j] = s1[i]
                i+=1
            else:
                s[i+j] = s2[j]
                j += 1

    def mergeSort(self, nums):
        length = len(nums)
        if length < 2: return

        mid = length//2
        nums1 = nums[:mid]
        nums2 = nums[mid:]

        self.mergeSort(nums1)
        self.mergeSort(nums2)

        self.merge(nums1, nums2, nums)

        return nums

# 自下而上的非递归版本
class Solution2:

    def mergeSort(self, nums):

        i = 1
        while i < len(nums):

            low = 0
            while low < len(nums):
                mid = low + i
                height = min(low + 2*i, len(nums))
                if mid <= height:
                    self.merge(nums, low, mid, height)
                low += 2*i

            i *= 2

        return nums

    def merge(self, nums, low, mid, height):
        nums1 = nums[low:mid]
        nums2 = nums[mid:height]
        i = j = 0

        # offset = low
        # while offset < height:
        #     if j == len(nums2) or (i < len(nums1) and nums1[i] <= nums2[j]):
        #         nums[offset] = nums1[i]
        #         i+=1
        #     else:
        #         nums[offset] = nums2[j]
        #         j += 1
        #     offset += 1

        for k in range(low, height):
            if j == len(nums2) or (i < len(nums1) and nums1[i] <= nums2[j]):
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1

# 链表实现非递归归并排序.
# class Solution3:
#
#     def mergeSort(self, root):
#         pass
#
#     def merge(self):
#         pass

from tools.analysis import ListNode
# 链表实现递归排序
class Solution3:

    def mergeSort(self, root):
        if root is None or root.next is None:
            return root
        head = root
        mid = self.findmid(head)
        tail = mid.next
        mid.next = None
        node = self.merge(self.mergeSort(head), self.mergeSort(tail))
        return node

    def findmid(self, root):
        head = ListNode(None)
        head.next = root
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, n1, n2):
        head = ListNode(None)
        root = head

        while n1 or n2:
            if n2 is None or (n1 is not None and n1.val <= n2.val):
                head.next = n1
                n1 = n1.next
            else:
                head.next = n2
                n2 = n2.next

            head = head.next
        return root.next

import pprint
# 测试以下deque, orderDict
class DequeTest:

    def work(self):
        from collections import deque
        d = deque(maxlen=10)
        d.append(1)
        d.append(2)
        d.appendleft(3)
        print(len(d))
        print(d[1])
        print(d[2])
        print(d.maxlen)
        print(d[0], d[1], d[2])
        d.rotate(1)
        print(d[0], d[1], d[2])
        pass

# OrderedDict 是按照输入顺序排序, 实际实现是一个按照输入依次输出的数组.
class OrderDictTest:

    def work(self):
        from collections import OrderedDict
        od = OrderedDict()
        od[1] = 3
        print(od)
        print(list(od.values()))
        print(dict(od))
        for k,v in od.items():
            print(k, v)



if __name__ == '__main__':
    # print(Solution().mergeSort([3, 4, 5, 2, 6, 1]))
    # print(Solution2().mergeSort([4, 3, 5, 2, 6, 1]))
    from tools.analysis import analysis_listnode
    print(Solution3().mergeSort(analysis_listnode([4, 3, 5, 2, 6])))
    # OrderDictTest().work()