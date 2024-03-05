from util import get_data

data = get_data(__file__)

info, graphs = data.split('\n', 1)
n_vertices, n_edges = map(int, info.split())
graphs = list(map(lambda x: list(map(int, x.split())), graphs.split('\n')))

def get_length_of_lowest_weight_path(start_vertex):
    length_of_shortest_paths = [None] * n_vertices
    length_of_shortest_paths[start_vertex - 1] = 0
    queue = [start_vertex]
    while queue:
        vertex = queue.pop(0)
        for edge in graphs:
            if vertex == edge[0]:
                neighbor = edge[1]
                if length_of_shortest_paths[neighbor - 1] == None:
                    length_of_shortest_paths[neighbor - 1] = length_of_shortest_paths[vertex - 1] + edge[2]
                    queue.append(neighbor)
                else:
                    if length_of_shortest_paths[neighbor - 1] > length_of_shortest_paths[vertex - 1] + edge[2]:
                        queue.append(neighbor)
                    length_of_shortest_paths[neighbor - 1] = min(length_of_shortest_paths[neighbor - 1], length_of_shortest_paths[vertex - 1] + edge[2])
                    
    for i in range(len(length_of_shortest_paths)):
        if length_of_shortest_paths[i] == None:
            length_of_shortest_paths[i] = -1
    return length_of_shortest_paths


length_of_shortest_paths = get_length_of_lowest_weight_path(1)
print(' '.join(map(str, length_of_shortest_paths)))

with open('Algorithmic_Heights/output/17_DIJ.txt', 'w') as f:
  f.write(' '.join(map(str, length_of_shortest_paths)) + '\n')
