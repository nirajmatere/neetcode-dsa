# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2
        if not l2: 
            return l1
        
        carry = 0 
        head = ListNode(0)
        temp = head
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = 0
            if add > 9:
                carry = 1
                add = add - 10
            
            node = ListNode(add)
            temp.next = node
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                add = l1.val + carry
                carry = 0
                if add > 9:
                    carry = 1
                    add = add - 10
                node = ListNode(add)
                temp.next = node
                temp = temp.next
                l1 = l1.next
        if l2:
            while l2:
                add = l2.val + carry
                carry = 0
                if add > 9:
                    carry = 1
                    add = add - 10
                node = ListNode(add)
                temp.next = node
                temp = temp.next
                l2 = l2.next
        
        if carry == 1:
            node = ListNode(1)
            temp.next = node
        return head.next
        









