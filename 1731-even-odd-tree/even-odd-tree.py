# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            prev_value = None

            for i in range(level_size):
                node = queue.popleft()
                
                # if the level is odd or Even
                if level % 2 == 0:
                    if node.val % 2 == 0 or (prev_value is not None and node.val <= prev_value):
                        return False
                else:
                    if node.val % 2 != 0 or (prev_value is not None and node.val >= prev_value):
                        return False
                
                prev_value = node.val

                # check child nodes 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return True