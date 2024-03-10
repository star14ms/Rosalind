from util import get_data

data = get_data("30_SCC.py")
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


def get_length_of_lowest_weight_path(graph, n_vertices, n_edges, offset):
  pos_graph = [None] * n_edges
  pos_graph[offset] = 0
  pos = [None] * n_vertices
  pos[graph[offset][0]-1] = 0
  pos[graph[offset][1]-1] = 1
  max_positon = 0

  queue = [graph[offset][1]-1]
  while queue:
    now = queue.pop(0)
    for node in filter(lambda x: x[0]-1 == now and graph.index(x) != offset, graph):
      next = node[1]-1
      if pos[next] == None or pos[next] > pos[now] + 1:
        pos[next] = pos[now] + 1
        pos_graph[graph.index(node)] = pos[now]
        queue.append(next)
      elif next == graph[offset][0]-1:
        pos_graph[graph.index(node)] = pos[now]
        max_positon = pos[now]
        queue = []
        break

  sorted_graph = [graph[offset][0], graph[offset][1]]

  for cursor in range(max_positon, 0, -1):
    i = list(filter(
      lambda i: pos_graph[i] == cursor and sorted_graph[0] == graph[i][1], 
      range(len(pos_graph))
    ))[0]
    next_vertex = graph[i][0]
    sorted_graph.insert(0, next_vertex)

  return sorted_graph


def remove_duplicates(components):
  for i, component in enumerate(components):
    for j, other_component in enumerate(components):
      if i != j and set(component) & set(other_component) == set(component):
        components.pop(j)
        return remove_duplicates(components)
  return components


non_cyclic_vertices = set()
components = []

for i in range(n_edges):
  sorted_graph = get_length_of_lowest_weight_path(graph, n_vertices, n_edges, i)
  
  if sorted_graph[0] != sorted_graph[-1]:
    non_cyclic_vertices.union(sorted_graph)
  else:
    components.append(sorted_graph)
  print(i+1, n_edges, end='\r')
print()

components = remove_duplicates(components)
cyclic_numbers = []
for component in components:
  cyclic_numbers.extend(component)

none_cyclic_numbers = set(non_cyclic_vertices) - set(cyclic_numbers)
print(len(components) + len(none_cyclic_numbers))