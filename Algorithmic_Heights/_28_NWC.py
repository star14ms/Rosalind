from util import get_data

data = get_data(__file__)
# data = '''2

# 4 5
# 1 4 4
# 4 2 3
# 2 3 1
# 3 1 6
# 2 1 -7

# 3 4
# 1 2 -8
# 2 3 20
# 3 1 -1
# 3 2 -30'''
# graphs = data.split('\n\n')[1:]
# graphs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), graphs))

lines = data.split('\n')[1:]
graphs = []

resume_index = 0
for i, line in enumerate(lines):
  if len(line.split(' ')) == 2 or i == len(lines)-1:
    graphs.append(lines[resume_index:i])
    resume_index = i

graphs = list(map(lambda graph: list(map(lambda node: list(map(int, node.split())), graph)), graphs[1:]))


def bellman_ford(n, edges, vertices_visited, offset=1):
    # Initialize distance array with infinity for all vertices
    # Assuming vertex numbering starts from 1, we adjust the array size accordingly
    dist = [float('inf')] * (n + 1)
    dist[offset] = 0  # Assuming the problem uses 1-indexing and we choose vertex 1 as the starting point

    # Relax edges repeatedly
    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return 1, vertices_visited  # Negative weight cycle found
    
    for i in range(n-1):
        if dist[i] != float('inf'):
            vertices_visited.add(i)

    return -1, vertices_visited # No negative weight cycle found


results = []

for graph in graphs:
    vertices_visited = set()
    n, m = graph.pop(0)

    for i in range(1, n+1):
        print(i, n, end='\r')
        if i in vertices_visited:
            continue
        result, vertices_visited = bellman_ford(n, graph, vertices_visited, i)
        if result == 1:
            break

    results.append(result)
    print(result, i, n)


print(' '.join(map(str, results)))
