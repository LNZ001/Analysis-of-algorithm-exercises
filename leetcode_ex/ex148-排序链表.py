from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None: return head
#         length = 1
#         root = ListNode(None)
#         root.next = head
#
#         while True:
#             last_node = root
#             left = root.next
#             pos = 0
#             right = left
#             while right is not None:
#                 if pos == length: break
#                 right = right.next
#                 pos += 1
#
#             else:
#                 break
#
#             # ########## 某一轮merge. ##########
#             while True:
#                 l, r = 0, 0
#                 lcur, rcur = left, right
#                 cur = last_node
#                 while l != length and r != length and rcur is not None:
#                     # ########## merge. ##########
#                     if lcur.val <= rcur.val:
#                         cur.next = lcur
#                         l += 1
#                         lcur = lcur.next
#                     else:
#                         cur.next = rcur
#                         r += 1
#                         rcur = rcur.next
#                     cur = cur.next
#
#                 if l == length:
#                     cur.next = rcur
#                     while r + 1 != length and rcur.next is not None:
#                         rcur = rcur.next
#                         r += 1
#                     last_node = rcur
#                     left = rcur.next
#                 elif r == length:
#                     left = cur.next
#                     cur.next = lcur
#                     tmp = lcur
#                     while l + 1 != length:
#                         tmp = tmp.next
#                         l += 1
#                     last_node = tmp
#                     last_node.next = left
#                 else:
#                     # ########## 达到本轮截止. ##########
#                     cur.next = lcur
#                     tmp = lcur
#                     while l + 1 != length:
#                         tmp = tmp.next
#                         l += 1
#                     tmp.next = None
#                     break
#
#                 if left is None: break
#
#                 pos = 0
#                 right = left
#                 while right is not None:
#                     if pos == length: break
#                     right = right.next
#                     pos += 1
#                 else:
#                     break
#
#             length *= 2
#
#         return root.next

'''
排序链表利用归并可以很快求解. 没有移动位置的成本. (还需要练一下从下往上的数组归并.)
'''
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        small, mid, big = None, None, None  # the tails, then insert before
        cur = head
        while cur:
            tmp = cur
            cur = cur.next  # move the pointer first, else it will be modified along with tmp
            if tmp.val < head.val:
                tmp.next = small
                small = tmp
            elif tmp.val > head.val:
                tmp.next = big
                big = tmp
            elif tmp.val == head.val:
                tmp.next = mid
                mid = tmp
            # cur = cur.next => wrong answer

        big = self.sortList(big)
        small = self.sortList(small)

        ret = ListNode(None)
        cur = ret

        for p in [small, mid, big]:
            while p is not None:
                cur.next = p
                p = p.next
                cur = cur.next
                cur.next = None
        return ret.next

if __name__ == '__main__':
    from tools.analysis import analysis_listnode
    print(Solution().sortList(analysis_listnode("-1->5->3->4->0")))