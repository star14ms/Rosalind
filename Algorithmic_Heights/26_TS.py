from util import get_data
from collections import defaultdict

data = get_data(__file__)
# data = '''4 5
# 1 2
# 3 1
# 3 2
# 4 3
# 4 2'''

graph = [list(map(int, x.split())) for x in data.split('\n')]

# Function to add edge into the graph
def addEdge(graph, u, v):
    graph[u].append(v)

# Function to perform DFS from a given vertex u
def dfs(u, visited, stack, graph):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, visited, stack, graph)
    stack.insert(0, u)  # Prepend current vertex to stack

# Function to perform topological sort
def topologicalSort(vertices, edges):
    graph = defaultdict(list)
    visited = [False] * (vertices + 1)
    stack = []

    # Adding edges to the graph
    for u, v in edges:
        addEdge(graph, u, v)
    
    # Perform DFS from all unvisited nodes to cover disconnected graphs
    for i in range(1, vertices + 1):
        if not visited[i]:
            dfs(i, visited, stack, graph)
    
    return stack

# Input
vertices = graph[0][0]  # Number of vertices
edges = graph[1:]  # Edges in the graph

# Perform topological sort
order = topologicalSort(vertices, edges)

# Output
print(" ".join(map(str, order)))

with open('Algorithmic_Heights/output/26_TS.txt', 'w') as output_data:
    output_data.write(' '.join(map(str, order)) + '\n')
