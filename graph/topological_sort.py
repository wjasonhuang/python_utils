'''
Topological Sorting of A Directed Graph
DFS algorithm O(V + E)
https://en.wikipedia.org/wiki/Topological_sorting
'''

# Leetcode 210

from typing import List, Tuple

def topological_sort(graph: List[List[int]]) -> Tuple[bool, List[int]]:
    '''
        graph: directed graph, graphe[u] = [v where u -> v]
        visited[u]: 0 not visited, 1 visiting, 2 visited
    '''

    n, is_possible = len(graph), True
    visited, sorted_array = [0] * n, []
    
    def dfs(u):
        nonlocal is_possible
        
        if not is_possible: return
        if visited[u]:
            is_possible = visited[u] == 2
            return
        
        visited[u] = 1
        for v in graph[u]: dfs(v)
        visited[u] = 2
        sorted_array.append(u)
    
    for u in range(n): dfs(u)
    return (is_possible, sorted_array if is_possible else [])
