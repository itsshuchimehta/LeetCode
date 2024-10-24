"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val = 0, nxt = None):
        self.val = val
        self.next = nxt

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current= current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next















