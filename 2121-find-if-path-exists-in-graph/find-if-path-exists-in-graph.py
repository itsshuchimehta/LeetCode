class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Using DSF with stack (Iterative)
        if source == destination:
            return True
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)
        stk = [source]

        while stk:
            node = stk.pop()
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stk.append(nei_node)
                
                if nei_node == destination:
                    return True
        return False
        # TC: O(V+E)
        # SC: O(V+E)