"""
https://en.wikipedia.org/wiki/Strongly_connected_component
A directed graph is said to be strongly connected if every vertex is reachable from every other vertex.
A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph.

O(V + E) to find all the strongly connected components
https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
https://www.geeksforgeeks.org/strongly-connected-components/
https://cp-algorithms.com/graph/strongly-connected-components.html

SPOJ CAPCITY
"""

from typing import List


def Kosaraju(graph: List[List[int]]) -> List[int]:
    """
    Kosaraju's algorithm O(V + E)
    graph: directed graph, graph[u] = [v where u -> v]
    return the number of scc and the partition of vertices
    """

    n = len(graph)
    order, visited = [], [False] * n
    for u in range(n):
        if visited[u]: continue
        visited[u] = True
        stack = [(u, 0)]
        while stack:  # use stack instead of dfs to avoid stack overflow from deep recursion
            cur, iter = stack.pop()
            if iter < len(graph[cur]):
                stack.append((cur, iter + 1))
                v = graph[cur][iter]
                if not visited[v]:
                    visited[v] = True
                    stack.append((v, 0))
            else:
                order.append(cur)
    gt = [[] for _ in range(n)]  # transpose of graph
    for u in range(n):
        for v in graph[u]:
            gt[v].append(u)
    scc, cnt = [-1] * n, 0
    for u in reversed(order):
        if scc[u] >= 0: continue
        scc[u] = cnt
        q = [u]
        while q:
            for v in gt[q.pop()]:
                if scc[v] < 0:
                    scc[v] = cnt
                    q.append(v)
        cnt += 1
    return cnt, scc


'''
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
'''

# To implement
