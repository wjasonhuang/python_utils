"""
Minimum Spanning Tree Kruskal's Algorithm O(|E|log|V|)
https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
"""

from union_find_set import UnionFindSet


def MSTKruskal(n, e):
    """
    n: vertices numbered 0..n-1
    e: list of [v1, v2, c] edge between v1 and v2 at cost c
    return: minimum spanning tree cost (assuming graph is connected)
    """

    e.sort(key=lambda i: i[2])
    ufs = UnionFindSet(n)
    MST = 0
    for v1, v2, c in e:
        if not ufs.union(v1, v2): MST += c
    return MST
