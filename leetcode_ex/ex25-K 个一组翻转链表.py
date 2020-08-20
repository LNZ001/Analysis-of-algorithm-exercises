from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    def single_reverseKGroup(self, init_node, k):
        if init_node is None or init_node.next is None: return
        cur = init_node
        check = init_node

        pos = -1
        while check:
            check = check.next
            pos += 1
            if pos == k: break
        else:
            # ########## 没有达到数量. ##########
            return

        # ########## 达到数量，反转. ##########
        pos = 0
        left = cur
        right = cur.next
        last_node = right
        while left and pos < k:
            tmp = right.next
            right.next = left

            left = right
            right = tmp
            pos += 1

        cur.next = left
        last_node.next = right
        self.single_reverseKGroup(last_node, k)


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1: return head
        init_node = ListNode(None)
        init_node.next = head

        self.single_reverseKGroup(init_node, k)
        return init_node.next


if __name__ == '__main__':
    from tools.analysis import analysis_listnode
    print(Solution().reverseKGroup(analysis_listnode([1, 2, 3, 4, 5]), 2))