# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Recursively
        def same(root1, root2):
            if not root1 and  not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            
            return same(root1.left, root2.right) and same(root1.right, root2.left)
        
        # return same(root, root)
        
        # iteratively

        stk = [root, root]

        while stk:
            node1 = stk.pop()
            node2 = stk.pop()
            
            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False
            
            # if (node1.left and not node2.right) or (node1.right and not node2.left) or (not node1.left and node2.right) or (not node1.right and  node2.left):
            if (node1.left is None) != (node2.right is None) or (node1.right is None) != (node2.left is None):
                return False

            if node1.left and node2.right:
                stk.append(node2.right)
                stk.append(node1.left)
            if node1.right and node2.left:
                stk.append(node2.left)
                stk.append(node1.right)

            
        
        return True


            
