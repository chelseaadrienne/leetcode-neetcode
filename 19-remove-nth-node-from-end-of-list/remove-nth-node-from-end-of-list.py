# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = temp = head
        for i in range(n):
            current = current.next
        if not current:
            return head.next
        while current.next:
            current = current.next
            temp = temp.next
        temp.next = temp.next.next
        return head