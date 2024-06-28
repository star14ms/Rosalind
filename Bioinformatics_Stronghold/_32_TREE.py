from util import get_data

data = get_data(__file__)
n, edges = data.split('\n', 1)
edges = [tuple(map(int, x.split())) for x in edges.split('\n') if x]

print(n)
print(len(edges))

def find_disconnected_components(n, edges):
    # Create an adjacency list to represent the graph
    graph = {i: [] for i in range(1, n+1)}
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)

    # Helper function to perform DFS
    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)
                
    # Find the number of disconnected components
    visited = set()
    components = 0
    for i in range(1, n+1):
        if i not in visited:
            dfs(i, visited)
            components += 1
            
    return components

# Sample Dataset
# n = 10
# edges = [(1, 2), (2, 8), (4, 10), (5, 9), (6, 10), (7, 9)]

# Calculate the number of edges needed to be added to make the graph a tree
disconnected_components = find_disconnected_components(int(n), edges)
edges_to_add = disconnected_components - 1  # Subtract 1 because the last component does not need an edge to connect

print(edges_to_add)