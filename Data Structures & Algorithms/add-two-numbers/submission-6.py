# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        curr2 = l2
        carry = 0
        prev = ListNode()
        pointer = prev

        while curr or curr2 or carry:
            v1 = curr.val if curr else 0
            v2 = curr2.val if curr2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            ones = val % 10

            prev.next = ListNode(ones)
            prev = prev.next

            if curr:
                curr = curr.next
            if curr2:
                curr2 = curr2.next
        return pointer.next





            
        

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

        



        