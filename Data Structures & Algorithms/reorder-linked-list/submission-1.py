# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return

        slow = fast = temp = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tmp = temp
        while tmp.next != slow:
            tmp = tmp.next
        tmp.next = None

        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head2 = prev
        head1 = head


        temp = head2
        while head1:
            temp = head2
            head2 = head2.next
            if temp.next != None:
                temp.next = head1.next
            head1.next = temp
            head1 = temp.next

        # while head1:
        #     print(head1.val)
        #     head1 = head1.next
        # print("HEAD2")
        # while head2:
        #     print(head2.val)
        #     head2 = head2.next
        
        amrit = head
        while amrit.next != None:
            amrit = amrit.next
        amrit.next = head2

        # head1.next = head2
        # return head
