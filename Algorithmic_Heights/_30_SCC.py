from util import get_data

data = get_data(__file__)
# data = '''6 7
# 4 1
# 1 2
# 2 4
# 5 6
# 3 2
# 5 3
# 3 5'''

info, graph = data.split('\n', 1)
n_vertices, n_edges = map(int, info.split())
graph = list(map(lambda x: list(map(int, x.split())), graph.split('\n')))

# number of strongly connected components
def dfs(graph, vertex, visited, stack=None):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    if stack is not None:
        stack.append(vertex)

def transpose_graph(graph, n):
    graph_t = {i: [] for i in range(n)}
    for vertex in graph:
        for neighbor in graph[vertex]:
            graph_t[neighbor].append(vertex)
    return graph_t

def kosaraju(n, edges):
    # Adjust for zero-based indexing
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        # Adjust vertices to zero-based index
        u, v = u - 1, v - 1
        graph[u].append(v)
    
    visited = [False] * n
    stack = []
    
    # First DFS pass to fill the stack with vertices by their finishing times
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, stack)
    
    # Generate the transpose graph
    graph_t = transpose_graph(graph, n)
    
    # Second DFS pass on the transpose graph
    visited = [False] * n
    scc_count = 0
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            dfs(graph_t, vertex, visited)
            scc_count += 1
    
    return scc_count

# Example Usage
print(kosaraju(n_vertices, graph))

