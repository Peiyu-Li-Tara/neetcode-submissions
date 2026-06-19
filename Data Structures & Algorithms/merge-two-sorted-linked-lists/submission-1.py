# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if not list1 and not list2:
            return None
        
        new_head = ListNode(-1)
        start = new_head
        curr1, curr2 = list1, list2
        while curr1 or curr2:
            if not curr1:
                tmp2 = curr2.next
                curr2.next = new_head.next
                new_head.next = curr2
                new_head = new_head.next
                curr2 = tmp2
            elif not curr2:
                tmp1 = curr1.next
                curr1.next = new_head.next
                new_head.next = curr1
                new_head = new_head.next
                curr1 = tmp1
            elif curr1.val < curr2.val:
                tmp1 = curr1.next
                curr1.next = new_head.next
                new_head.next = curr1
                new_head = new_head.next
                curr1 = tmp1
            else:
                tmp2 = curr2.next
                curr2.next = new_head.next
                new_head.next = curr2
                new_head = new_head.next
                curr2 = tmp2
        return start.next


