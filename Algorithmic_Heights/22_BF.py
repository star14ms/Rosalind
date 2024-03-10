from util import get_data, get_output_path

data = get_data(__file__)

# data = '''9 13
# 1 2 10
# 3 2 1
# 3 4 1
# 4 5 3
# 5 6 -1
# 7 6 -1
# 8 7 1
# 1 8 8
# 7 2 -4
# 2 6 2
# 6 3 -2
# 9 5 -10
# 9 4 7'''

info, graphs = data.split('\n', 1)
n_vertices, n_edges = map(int, info.split())
graphs = list(map(lambda x: list(map(int, x.split())), graphs.split('\n')))

# Bellman-Ford algorithm
def get_length_of_lowest_weight_path(graphs, n_vertices, start_vertex):
    shortest_lengths = [None] * n_vertices
    shortest_lengths[start_vertex - 1] = 0

    search_numbers = {start_vertex,}
    for i in range(n_vertices - 1):
        search_numbers_next = set()

        for edge in graphs:
            if shortest_lengths[edge[0] - 1] != None and edge[0] in search_numbers:
                search_numbers_next.add(edge[1])
                if shortest_lengths[edge[1] - 1] == None:
                    shortest_lengths[edge[1] - 1] = shortest_lengths[edge[0] - 1] + edge[2]
                else:
                    shortest_lengths[edge[1] - 1] = min(shortest_lengths[edge[1] - 1], shortest_lengths[edge[0] - 1] + edge[2])
        search_numbers = search_numbers_next

    for i in range(len(shortest_lengths)):
        if shortest_lengths[i] == None:
            shortest_lengths[i] = -1
    return shortest_lengths


shortest_lengths = get_length_of_lowest_weight_path(graphs, n_vertices, 1)
print(' '.join(map(str, shortest_lengths)))

with open(get_output_path(__file__), 'w') as f:
    f.write(' '.join(map(lambda x: str(x) if x != -1 else 'x', shortest_lengths)))