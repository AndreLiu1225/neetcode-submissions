# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head

        dummy = ListNode()
        dummy.next = head
        start = dummy

        while n > 0:
            end = end.next
            n -= 1

        while end:
            start = start.next
            end = end.next

        start.next = start.next.next
        return dummy.next
        



        