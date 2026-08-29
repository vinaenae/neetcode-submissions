# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        arr = []
        while curr:
            if curr.next and curr.next in arr:
                return True
            elif curr.next:
                arr.append(curr)
                curr = curr.next
            else:
                return False 
        return False



        