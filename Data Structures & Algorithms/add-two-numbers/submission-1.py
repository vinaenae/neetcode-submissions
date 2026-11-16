# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        curr2 = l2
        stack1, stack2 = [], []
        while curr and curr2:
            stack1.append(str(curr.val))
            stack2.append(str(curr2.val))
            curr = curr.next
            curr2 = curr2.next
        while curr:
            stack1.append(str(curr.val))
            curr = curr.next
        while curr2:
            stack2.append(str(curr2.val))
            curr2 = curr2.next
        

        val1 = int("".join(reversed(stack1)))
        val2 = int("".join(reversed(stack2)))
        output = str(val1 + val2)
        prev = ListNode()
        pointer = prev
        output2 = "".join(reversed(output))
        for i in range(len(output)):
            val = ListNode(output2[i])
            prev.next = val
            prev = prev.next
        return pointer.next

        



        