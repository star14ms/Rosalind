from util import get_data

data = get_data("31_GS.py")
# data ='''2

# 3 2
# 3 2
# 2 1

# 3 2
# 3 2
# 1 2'''
graphs = data.split('\n\n')[1:]
graphs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), graphs))


def get_min_vertex_connected(graph, n_vertex, offset=0):
  pos = [None] * n_vertex
  pos[graph[offset][0]-1] = 0
  pos[graph[offset][1]-1] = 1

  # right
  # queue = [graph[offset][1]-1]
  # while queue:
  #   now = queue.pop(0)
  #   for node in filter(lambda x: x[0]-1 == now and graph.index(x) != offset, graph):
  #     next = node[1]-1
  #     if pos[next] == None or pos[next] > pos[now] + 1:
  #       pos[next] = pos[now] + 1
  #       queue.append(next)

  # left
  queue = [graph[offset][0]-1]
  while queue:
    now = queue.pop(0)
    for node in filter(lambda x: x[1]-1 == now and graph.index(x) != offset, graph):
      next = node[0]-1
      if pos[next] == None or pos[next] < pos[now] - 1:
        pos[next] = pos[now] - 1
        queue.append(next)
  
  min_vertex = pos.index(min(filter(lambda x: x != None, pos))) + 1

  return min_vertex


def can_offset_reach_every_vertices(graph, n_vertices, vertex_offset=1):
    queue = [vertex_offset]
    visited = [False] * (n_vertices + 1)
    visited[vertex_offset] = True
  
    while queue:
        now = queue.pop(0)

        for n, v in filter(lambda x: x[0] == now, graph):
            if not visited[v]:
              # print(node)
              # breakpoint()
              visited[v] = True
              queue.append(v)

    return False not in visited[1:]


min_vertices = []

for graph in graphs:
  n_vertex, n_edge = graph.pop(0)
  min_vertex = get_min_vertex_connected(graph, n_vertex, 0)

  if can_offset_reach_every_vertices(graph, n_vertex, min_vertex):
    min_vertices.append(min_vertex)
  else:
    min_vertices.append(-1)

print(' '.join(map(str, min_vertices)))
