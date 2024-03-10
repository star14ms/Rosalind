from util import get_data

data = get_data('28_NWC.py')
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


def has_negetive_weight_cycle(graph, n_vertices, start_vertex):
    shortest_lengths = [None] * n_vertices
    shortest_lengths[start_vertex - 1] = 0

    def reduce_graph(graph, start_vertex):
      for node in graph:
        if node[0] == start_vertex - 1:
          graph.remove(node)
        if node[1] == start_vertex - 1:
          graph.remove(node)
      return graph

    search_numbers = {start_vertex,}
    for _ in range(n_vertices - 1):
        search_numbers_next = set()

        for now1, next1, weight in graph:
            now = now1 - 1
            next = next1 -1
            if shortest_lengths[now] != None and now1 in search_numbers:
                search_numbers_next.add(next1)
                if shortest_lengths[next] == None:
                    shortest_lengths[next] = shortest_lengths[now] + weight
                else:
                    shortest_lengths[next] = min(shortest_lengths[next], shortest_lengths[now] + weight)

            if shortest_lengths[now] != None and shortest_lengths[next] != None and shortest_lengths[now] + weight - shortest_lengths[next] < 0:
                return True, graph

        search_numbers = search_numbers_next
  
    return False, reduce_graph(graph, start_vertex)


has_negetive_cycles = []

for graph in graphs:
    n_vertices, n_edges = graph.pop(0)

    for start_vertex in range(1, n_vertices + 1):
        has_negetive_cycle, graph = has_negetive_weight_cycle(graph, n_vertices, start_vertex)
        print(len(graph), end='\r')
        if has_negetive_cycle:
            has_negetive_cycles.append(1)
            break
    else:
        has_negetive_cycles.append(-1)

    print(has_negetive_cycle)

print(' '.join(map(str, has_negetive_cycles)))
