### hard
from util import get_data

# data = '''2

# 4 5
# 2 4 2
# 3 2 1
# 1 4 3
# 2 1 10
# 1 3 4

# 4 5
# 3 2 1
# 2 4 2
# 4 1 3
# 2 1 10
# 1 3 4'''

# graphs = data.split('\n\n')[1:]
# graphs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), graphs))

data = get_data(__file__)

lines = data.split('\n')[1:]
graphs = []

resume_index = 0
for i, line in enumerate(lines):
  if len(line.split(' ')) == 2 or i == len(lines)-1:
    graphs.append(lines[resume_index:i])
    resume_index = i

graphs = list(map(lambda graph: list(map(lambda node: list(map(int, node.split())), graph)), graphs[1:]))


def get_length_of_full_cycle(graph):
  n_vertices = graph.pop(0)[0]
  offset = 0
  queue = [offset]
  distances_weight = [-1] * n_vertices
  distances_weight[offset] = 0
  distances = [-1] * n_vertices
  distances[offset] = 0

  while queue:
    u = queue.pop(0)

    for node in list(filter(lambda x: x[0] == u+1, graph)):
      v = node[1]
      if not v-1 == offset:
        if distances[v-1] != -1:
          distances[v-1] = min(distances[u] + 1, distances[v-1])
        else:
          distances[v-1] = distances[u] + 1
          queue.append(v-1)
        distances_weight[v-1] = distances_weight[u] + node[-1]
      elif v-1 == 0:
        return distances_weight[u] + node[-1]
  return -1


def get_length_of_shortest_cycle(graph, offset_node=0):
  n_vertices = graph.pop(0)[0]
  offset = graph[offset_node][0] - 1
  queue = [offset]
  lengths = [-1] * n_vertices
  lengths[offset] = 0
  lengths_of_cycles = []

  while queue:
    u = queue.pop(0)

    for node in list(filter(lambda x: x[0] == u+1, graph)):
      if node[0]-1 == offset and node[1] != graph[offset_node][1]:
        continue

      v = node[1]
      new_length = lengths[u] + node[-1]

      if v-1 == offset:
        lengths_of_cycles.append(new_length)
      elif lengths[v-1] == -1 or new_length < lengths[v-1]:
        lengths[v-1] = new_length
        queue.append(v-1)

  if lengths_of_cycles:
    return min(lengths_of_cycles)
  return -1


length_of_shortest_cycle = list(map(get_length_of_shortest_cycle, graphs))
print(*length_of_shortest_cycle)

