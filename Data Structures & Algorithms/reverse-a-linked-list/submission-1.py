class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        prev = None
        while start:
            val = start.next
            start.next = prev
            prev = start
            start = val
        return prev





        