class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        total = 0
        visited = [False] * n
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)

        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                total += 1

        return total