# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = [True]

        def height(root):
            if not root:
                return 0
            
            left_height = height(root.left)
            if balance[0] is False:
                return 0
            right_height = height(root.right)
            if abs(left_height - right_height) > 1:
                balance[0] = False
                return 0
            return 1 + max(left_height, right_height)
        
        height(root)
        return balance[0]