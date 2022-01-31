
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        seen = [False] * (n + 1)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([source, ])

        while q:
            node = q.popleft()

            seen[node] = True

            if node == destination:
                return True

            for u in graph[node]:
                if not seen[u]:
                    q.append(u)

        return False