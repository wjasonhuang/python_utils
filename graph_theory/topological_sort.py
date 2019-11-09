'''
Topological Sorting of A Directed Graph
https://en.wikipedia.org/wiki/Topological_sorting
A topological ordering is possible if and only if the graph has no directed cycles
'''


from typing import List, Tuple

'''
DFS algorithm O(V + E)
'''

def topological_sort(graph: List[List[int]]) -> Tuple[bool, List[int]]:
    '''
        graph: directed graph, graph[u] = [v where u -> v]
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


'''
Kahn's algorithm O(V + E), return in reverse order of DFS algorithm
'''

def Kahn(graph: List[List[int]]) -> Tuple[bool, List[int]]:
    '''
        graph: directed graph, graph[u] = [v where u -> v]
    '''
    
    n, idx = len(graph), 0
    degree, sorted_array = [0] * n, []
    
    for i in range(n):
        for j in graph[i]:
            degree[j] += 1
    for i in range(n):
        if degree[i] == 0: sorted_array.append(i)
    
    while idx < len(sorted_array):
        u = sorted_array[idx]
        for v in graph[u]:
            degree[v] -= 1
            if degree[v] == 0: sorted_array.append(v)
        idx += 1
    
    return (idx == n, sorted_array if idx == n else [])
