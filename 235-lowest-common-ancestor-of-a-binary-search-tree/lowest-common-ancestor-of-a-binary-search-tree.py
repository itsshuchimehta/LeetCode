# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]
        
        def dfs(node):
            if not node: 
                return 
            lca[0] = node
            if node is p or node is q:
                return
            elif node.val < p.val and node.val < q.val:
                dfs(node.right)
            elif node.val > p.val and node.val > q.val:
                dfs(node.left)
            else:
                return
                  
        dfs(root)

        return lca[0]
