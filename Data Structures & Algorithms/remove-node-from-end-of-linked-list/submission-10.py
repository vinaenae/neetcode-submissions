# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        start = head
        first = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        remove_elem = (count - n)
        loop_node = 0
        while start:
            if count == 1:
                first = None
                break
            elif (remove_elem - 1) == -1:
                first = start.next
                break
            else:
                if loop_node == remove_elem - 1:
                    start.next = start.next.next
                    break
                start = start.next
                loop_node += 1
        return first
        
        # curr = head
        # arr = []
        # while curr:
        #     arr.append(curr)
        #     curr = curr.next
        # start = 1
        # for i in range(len(arr) - 1, -1, -1):
        #     if start == n:
        #         del arr[i]
        #         break
        #     start += 1
        # for i in range(len(arr)):
        #     if i + 1 < len(arr):
        #         arr[i].next = arr[i+1]
        #     else:
        #         arr[i].next = None
        # if arr:
        #     return arr[0]
        # else:
        #     return curr
        

        
        