"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashmap = {}
        visited = set()
        visited.add(node)
        def dfs(n):
            hashmap[n] = Node(val = n.val)
            for nei in n.neighbors:
                if nei not in visited:
                    hashmap[nei] = Node(val = nei.val)
                    visited.add(nei)
                    dfs(nei)
        dfs(node)
        
        for old_node, new_node in hashmap.items():
            for nei in old_node.neighbors:
                new_nei = hashmap[nei]
                new_node.neighbors.append(new_nei)


        return hashmap[node]
