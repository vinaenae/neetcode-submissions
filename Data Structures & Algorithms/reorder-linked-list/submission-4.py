
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        curr = head
        fast = slow.next
        first = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        before = None
        slow.next = before
        while second:
            tmp = second.next
            second.next = before
            before = second
            second = tmp
        while before:
            tmp = curr.next
            tmp2 = before.next
            curr.next = before
            before.next = tmp
            curr = tmp
            before = tmp2

        
        
        

        