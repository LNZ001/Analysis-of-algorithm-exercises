from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        cur = head

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        cur.next = l1 if l1 else l2
        return head.next

if __name__ == '__main__':
    from tools.analysis import analysis_listnode
    print(Solution().mergeTwoLists(analysis_listnode([1, 2, 4]), analysis_listnode([1, 3, 4])))