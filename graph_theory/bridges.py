"""
https://en.wikipedia.org/wiki/Bridge_(graph_theory)

An edge in an undirected connected graph is a bridge if removing it disconnects the graph.
A bridge is an edge removing which increases number of disconnected components.

O(V + E) to find all bridges
We do DFS traversal of the given graph. In DFS tree an edge (u, v) (u is parent of v in DFS tree) is bridge 
if there does not exist any other alternative to reach u or an ancestor of u from subtree rooted with v.

https://www.geeksforgeeks.org/bridge-in-a-graph/
https://cp-algorithms.com/graph/bridge-searching.html

Leetcode 1192
"""

def criticalConnections(self, n, edges):
    g = dict()
    for i in range(n): g[i] = []
    for e in edges:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    ret = []
    disc = [0] * n
    low = [0] * n
    visited = [False] * n
    self.time = 0

    def dfs(u, p):
        visited[u] = True
        disc[u] = low[u] = self.time
        self.time += 1
        for v in g[u]:
            if not visited[v]:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]: ret.append([u, v])
            elif v != p:
                low[u] = min(low[u], low[v])

    for i in range(n):
        if not visited[i]: dfs(i, -1)
    return ret
