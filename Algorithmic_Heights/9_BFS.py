from util import get_data

data = get_data(__file__)

edges = data.split('\n')
vertex_count, edge_count = map(int, edges[0].split())
edges = [tuple(map(int, edge.split())) for edge in edges[1:]]


def get_length_of_shortest_paths(start_vertex):
    length_of_shortest_paths = [None] * vertex_count
    length_of_shortest_paths[start_vertex - 1] = 0
    queue = [start_vertex]
    while queue:
        vertex = queue.pop(0)
        for edge in edges:
            if vertex == edge[0]:
                neighbor = edge[0]
                if length_of_shortest_paths[neighbor - 1] == None:
                    length_of_shortest_paths[neighbor - 1] = length_of_shortest_paths[vertex - 1] + 1
                    queue.append(neighbor)
                    
    for i in range(len(length_of_shortest_paths)):
        if length_of_shortest_paths[i] == None:
            length_of_shortest_paths[i] = -1
                    
    return length_of_shortest_paths
  

length_of_shortest_paths = get_length_of_shortest_paths(1)
print(' '.join(map(str, length_of_shortest_paths)))