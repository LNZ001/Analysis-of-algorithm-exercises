# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        h = ListNode(None)
        h.next = head


        pre = h
        left = head
        right = head.next
        while True:
            if right is None:
                # ########## 直接返回. ##########
                pre.next = left
                break

            tmp = right.next
            pre.next = right
            right.next = left

            if tmp is None:
                left.next = tmp
                break
            pre = left
            left = tmp
            right = tmp.next

        return h.next

if __name__ == '__main__':
    from tools import analysis
    print(Solution().swapPairs(analysis.analysis_listnode([1, 2, 3, 4])))


