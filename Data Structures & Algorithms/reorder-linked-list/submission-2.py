
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        left = 0
        right = len(arr) - 1
        values = ListNode()
        while left <= right:
            values.next = arr[left]
            values = values.next
            left += 1
            if left > right:
                values.next = None
                break
            values.next = arr[right]
            values = values.next
            right -= 1
        values.next = None
        
        

        