# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[1]
        
        # solution with extra array O(n) space
        array = []
        for li in lists:
            head = li
            while head:
                array.append(head.val)
                head = head.next
        
        # print(array)
        array.sort()
        newHead = ListNode(array[0])
        temp = newHead
        for i in range(1, len(array)):
            node = ListNode(array[i])
            temp.next = node
            temp = temp.next
        
        return newHead










