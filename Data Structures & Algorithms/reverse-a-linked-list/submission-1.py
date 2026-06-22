# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iteratively:
        dummy_head = ListNode()

        while head:
            tmp = head.next
            head.next = dummy_head.next
            dummy_head.next = head
            head = tmp
        
        return dummy_head.next
