'''
Maximum Flow - Ford–Fulkerson algorithm O(E max|f|)
https://en.wikipedia.org/wiki/Maximum_flow_problem
https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

Applicaiton:
    Bipartite Matching O(V^3)
    Minimum Cut of A Network Flow - nodes reachable from souce in max flow residual graph vs the rest
'''

# SPOJ 377

def FordFulkerson(source, sink, graph, flow):   
    # graph[u]: list of v such that u -> v exists
    # flow[(u, v)]: residual capacity of edge u -> v
    parent, max_flow = [-1] * (len(graph)), 0

    def BFS(s, t, parent): # return True if there is path from s to t in residual graph
        visited, queue = [False] * (len(graph)), []
        queue.append(s) 
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for v in graph[u]:
                if not visited[v] and flow[(u, v)] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
            if visited[t]: return True
        return False

    # augment the flow while there is path from source to sink 
    while BFS(source, sink, parent):
        path_flow, s = 10000, sink
        while s != source:
            path_flow = min(path_flow, flow[(parent[s], s)])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v !=  source:
            u = parent[v]
            flow[(u, v)] -= path_flow
            flow[(v, u)] += path_flow
            v = parent[v]

    return max_flow
