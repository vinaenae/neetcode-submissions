
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        start = slow.next
        
        while second_half:
            cur = second_half.next
            second_half.next = start
            start = second_half
            second_half = cur

        begin = head
        while start:
            val, prev = begin.next, start.next
            begin.next = start
            start.next = val
            start, begin = prev, val
        
                            
        
        
        
        

        