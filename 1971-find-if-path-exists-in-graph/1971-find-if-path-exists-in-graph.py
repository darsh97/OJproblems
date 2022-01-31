class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        seen = [False] * (n + 1)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(v):
            nonlocal seen
            seen[v] = True

            if v == destination:
                return True

            for u in graph[v]:
                if not seen[u] and dfs(u):
                    return True

            return False
        
        return dfs(source)
