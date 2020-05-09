"""
Single-source shortest paths
    Unweighted graphs: BFS O(E + V)
    Directed graphs with non-negative weights: Dijkstra O(E + VlogV)
    Directed graphs with arbitrary weights: Bellman–Ford O(VE)
    Weighted directed acyclic graphs: topological sorting O(E + V)

All-pairs shortest paths
    Floyd–Warshall O(V^3)
    Johnson–Dijkstra O(EV + V^2logV)
"""

from typing import List, Tuple

MAX_DIST = 10 ** 9

'''
Dijkstra's algorithm - O(V^2) or O(E + VlogV) using Fibonacci heap
Fastest single-source shortest-path algorithm for arbitrary directed graphs with unbounded non-negative weights
'''


def Dijkstra(graph: List[List[int]], source) -> Tuple[List[int], List[int]]:
    """
    graph: directed graph, graph[u] = [(v, c) where u -> v with cost c]
    """

    n = len(graph)
    dist, prev, queue = [MAX_DIST] * n, [-1] * n, set(range(n))
    dist[source] = 0
    while queue:
        u = -1
        for i in queue:
            if u == -1 or dist[i] < dist[u]: u = i
        queue.remove(u)
        for v, c in graph[u]:
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                prev[v] = u
    return dist, prev


'''
Bellman–Ford algorithm - O(VE)
Capable of handling graphs in which some of the edge weights are negative numbers
'''


def Bellman_Ford(edges: List[List[int]], n_vertices, source) -> Tuple[bool, List[int], List[int]]:
    """
    vertices: 0, 1, ..., n_vertices - 1
    edges: list of edges in format (u, v, c), u -> v with cost c
    return (False, None, None) if negative cycle exists, else (True, distances, paths)
    """

    dist, prev = [MAX_DIST] * n_vertices, [-1] * n_vertices
    dist[source] = 0
    for _ in range(n_vertices - 1):
        for u, v, c in edges:
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                prev[v] = u
    for u, v, c in edges:
        if dist[v] > dist[u] + c: return False, [], []
    return True, dist, prev


'''
Floyd–Warshall O(V^3)
Find shortest distances between every pair of vertices
'''


def Floyd_Warshall(graph: List[List[int]]) -> List[List[int]]:
    """
    graph[u][v]: cost u -> v
    """

    n = len(graph)
    dist = [graph[i][:] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


'''
Johnson–Dijkstra O(EV + V^2logV)
1) Add a new vertex s and edges from s to all vertices of the graph
2) Let h[0], h[1], ..., h[V-1] be the distances calculated by Bellman-Ford for vertex s
3) For an edge (u, v) of weight w(u, v), the new weight becomes w(u, v) + h[u] – h[v]
4) All set of paths between any two vertices are increased by same amount
5) All negative weights become non-negative, because h is the shortest distance h[v] <= h[u] + w(u, v)
6) Remove s and run Dijkstra's algorithm for every vertex 
'''

# To implement

'''
#LeetCode 743
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = [[] for _ in range(N)]
        for u, v, c in times:
            g[u - 1].append((v - 1, c))
        dist, _ = Dijkstra(g, K - 1)
        ret = max(dist)
        return ret if ret != MAX_DIST else -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        for i in range(len(times)):
            times[i][0] -= 1
            times[i][1] -= 1
        _, dist, _ = Bellman_Ford(times, N, K - 1)
        ret = max(dist)
        return ret if ret != MAX_DIST else -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = [[MAX_DIST] * N for _ in range(N)]
        for i in range(N): g[i][i] = 0
        for u, v, c in times: g[u-1][v-1] = c
        dist = Floyd_Warshall(g)
        ret = max(dist[K-1])
        return ret if ret != MAX_DIST else -1
'''
