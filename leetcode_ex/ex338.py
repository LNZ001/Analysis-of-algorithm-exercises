from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:

        G = set(G)
        count = 0
        length = 0
        isValid = False

        cur = head
        while cur:
            if cur.val not in G:
                if isValid:
                    count+= 1
                    isValid = False
            else:
                isValid = True

            cur = cur.next
        if isValid:
            count += 1

        return count

if __name__ == '__main__':
    print(Solution().numComponents(ListNode(0, ListNode(1, ListNode(2, ListNode(3)))), [0,1,3]))