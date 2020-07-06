from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, start):
        node = start
        last = None
        while node:
            node.next, last, node = last, node, node.next


    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return None

        fast = head
        slow = head
        while fast.next is not None:
            if fast.next.next is None:
                fast = fast.next
                slow.next, slow = None, slow.next
                break

            fast = fast.next.next
            slow = slow.next
        else:
            slow.next, slow = None, slow.next

        # ########## 反转链表 ##########
        self.reverseList(slow)


        # ########## 合并链表, 两个开头实际是head和fast ##########
        last_node = None
        left = head
        right = fast
        while left is not None:
            if right is None:
                last_node.next = left
                left.next = None
                return None

            tmp_left = left.next
            tmp_right = right.next

            if last_node is not None:
                last_node.next = left
            left.next = right
            last_node = right

            left = tmp_left
            right = tmp_right

        return None

if __name__ == '__main__':
    print(Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))