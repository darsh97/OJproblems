class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_count = len(edges)
        graph = defaultdict(int)

        for u, v in edges:
            graph[u] += 1
            graph[v] += 1

        for k, v in graph.items():
            if v == edge_count:
                return k