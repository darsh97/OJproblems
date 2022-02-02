class UnionFind:
    def __init__(self, size):
        self._parent = [*range(size)]
        self._rank = [0] * size

    def find(self, node):
        if self._parent[node] != node:
            self._parent[node] = self.find(self._parent[node])
        return self._parent[node]

    def union(self, current_node, other_node):
        pcn, pon = self.find(current_node), self.find(other_node)
        self._parent[other_node] = current_node

    @property
    def get_parent(self):
        return self._parent

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)

        return list(set(map(uf.find, uf.get_parent)))
