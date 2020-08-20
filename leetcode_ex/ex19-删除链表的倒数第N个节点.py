from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        init_node = ListNode(None)
        init_node.next = head

        fast = init_node
        slow = init_node

        for i in range(n):
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return init_node.next

if __name__ == '__main__':
    from tools.analysis import analysis_listnode
    print(Solution().removeNthFromEnd(analysis_listnode([1, 2, 3, 4, 5]), 2))