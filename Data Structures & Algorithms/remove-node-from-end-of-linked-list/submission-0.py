# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        start = 1
        for i in range(len(arr) - 1, -1, -1):
            if start == n:
                del arr[i]
                break
            start += 1
        for i in range(len(arr)):
            if i + 1 < len(arr):
                arr[i].next = arr[i+1]
            else:
                arr[i].next = None
        if arr:
            return arr[0]
        else:
            return curr
        

        
        