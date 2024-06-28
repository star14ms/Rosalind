from util import get_data, get_output_path

input_data = get_data(__file__)
# data ='''2

# 3 3
# 1 2
# 2 3
# 1 3

# 4 3
# 4 3
# 3 2
# 4 1'''

# graphs = data.split('\n\n')[1:]
# graphs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), graphs))

from collections import defaultdict

def topological_sort(num_vertices, edges):
    graph = defaultdict(list)
    in_degree = [0] * (num_vertices + 1)
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Find all vertices with 0 in-degree to start the sort
    queue = [v for v in range(1, num_vertices + 1) if in_degree[v] == 0]
    topo_order = []
    
    while queue:
        u = queue.pop(0)
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if len(topo_order) == num_vertices:
        return topo_order
    else:
        return []

def check_hamiltonian_path(num_vertices, edges):
    topo_order = topological_sort(num_vertices, edges)
    if not topo_order:
        return "-1"
    
    edge_set = set(edges)
    for i in range(len(topo_order) - 1):
        if (topo_order[i], topo_order[i + 1]) not in edge_set:
            return "-1"
    
    return "1 " + " ".join(map(str, topo_order))

# # Input processing
# input_data = """2

# 3 3
# 1 2
# 2 3
# 1 3

# 4 3
# 4 3
# 3 2
# 4 1"""


# Split the input data into lines and process each graph
lines = input_data.split('\n')
i = 1  # Skip the first line (number of graphs)
results = []

while i < len(lines):
    if lines[i].strip() == '':
        i += 1
        continue
    
    n, m = map(int, lines[i].split())
    edges = []
    for j in range(1, m + 1):
        edges.append(tuple(map(int, lines[i + j].split())))
    i += m + 1
    results.append(check_hamiltonian_path(n, edges))

# Output results
for result in results:
    print(result)

with open(get_output_path(__file__), 'w') as output_data:
    output_data.write('\n'.join(results) + '\n')
