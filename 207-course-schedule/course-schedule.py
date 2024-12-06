class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        course = prerequisites
        for a, b in course:
            g[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]

            if state == VISITING: return False
            if state == VISITED: return True

            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        # TC: O(N+E)
        # SC: O(N)