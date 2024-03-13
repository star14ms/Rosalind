### hard
from util import get_data

data = get_data(__file__)
data ='''2

3 2
3 2
2 1

3 2
3 2
1 2'''
graphs = data.split('\n\n')[1:]
graphs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), graphs))


def dfs(graph, vertex, visited):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def find_mother_vertex(n, edges):
    # Build the graph
    graph = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * (n + 1)
    last_visited = 0
    # Perform DFS and find the last finished vertex
    for i in range(1, n+1):
        if not visited[i]:
            dfs(graph, i, visited)
            last_visited = i
    
    # Check if the last finished vertex can reach all vertices
    visited = [False] * (n + 1)
    dfs(graph, last_visited, visited)
    
    if all(visited[1:]):  # Exclude the dummy 0 index
        return last_visited
    else:
        return -1


results = []

for graph in graphs:
  n_vertex, n_edge = graph.pop(0)

  result = find_mother_vertex(n_vertex, graph)
  results.append(result)

print(' '.join(map(str, results)))



