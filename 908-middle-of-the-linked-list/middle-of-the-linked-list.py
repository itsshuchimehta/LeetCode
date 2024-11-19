# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = []
        cur = head

        while cur:
            if cur not in visited:
                visited.append(cur)
                cur = cur.next
        
        if cur is None:
            n = len(visited) 
            m = n // 2
            cur = visited[m]
        return cur