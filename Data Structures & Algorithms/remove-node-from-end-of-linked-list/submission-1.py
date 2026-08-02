# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        idx_remove = len(nodes) - n
        if idx_remove == 0:
            return head.next

        nodes[idx_remove - 1].next = nodes[idx_remove].next
        return head