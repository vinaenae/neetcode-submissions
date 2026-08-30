
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        original = ListNode()
        curr = head
        arr = []
        original.next = curr
        while curr:
            arr.append(curr)
            curr = curr.next
        left = 0
        right = len(arr) - 1
        values = original
        while left <= right:
            values.next = arr[left]
            values = values.next
            left += 1
            if left > right:
                values.next = None
                break
            values.next = arr[right]
            print(values.next.val)
            values = values.next
            right -= 1
        values.next = None
        
        

        