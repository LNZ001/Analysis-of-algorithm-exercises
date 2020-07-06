from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        fast = head
        slow = head

        if fast is None or fast.next is None:
            return None
        if fast.next == fast:
            return fast

        fast = fast.next.next
        slow = slow.next

        while fast != slow:
            if fast is None or fast.next is None:
                return None

            fast = fast.next.next
            slow = slow.next

        while head != slow:
            head = head.next
            slow = slow.next

        return head


if __name__ == '__main__':
    print(Solution().detectCycle(...))