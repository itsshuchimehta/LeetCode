from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Using BFS with Queue (Iterative)
        if source == destination:
            return True
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)
        q = deque()
        q.append(source)

        while q:
            node = q.popleft()
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)
                
                if nei_node == destination:
                    return True
        return False
        # TC: O(V+E)
        # SC: O(V+E)