from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (head == None or head.next == None): return False
        fast = head.next
        slow = head

        while fast != slow:
            if fast is not None and fast.next is not None and slow is not None:
                fast = head.next.next
                slow = head.next
            else:
                return False
        return True


if __name__ == '__main__':
    print(Solution().hasCycle(...))