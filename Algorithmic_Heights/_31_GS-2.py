from util import get_data

data = get_data("31_GS.py")
data ='''2

3 2
3 2
2 1

3 2
3 2
1 2'''
graphs = data.split('\n\n')[1:]
graphs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), graphs))

def is_graph_all_connected(graph, n_vertex, vertices_visited, offset=0):
  pos = [None] * n_vertex
  pos[graph[offset][0]-1] = 0
  pos[graph[offset][1]-1] = 1

  # right
  queue = [graph[offset][1]-1]
  while queue:
    now = queue.pop(0)
    for node in filter(lambda x: x[0]-1 == now and graph.index(x) != offset, graph):
      next = node[1]-1
      if pos[next] == None or pos[next] > pos[now] + 1:
        pos[next] = pos[now] + 1
        queue.append(next)

  # left
  queue = [graph[offset][0]-1]
  while queue:
    now = queue.pop(0)
    for node in filter(lambda x: x[1]-1 == now and graph.index(x) != offset, graph):
      next = node[0]-1
      if pos[next] == None or pos[next] < pos[now] - 1:
        pos[next] = pos[now] - 1
        queue.append(next)

  for i in range(len(pos)):
    if pos[i] != None:
        vertices_visited.add(i)

  if None in pos:
    return -1, pos.index(min(pos)) + 1
  
  return 1, pos.index(min(pos)) + 1


is_all_connected_list = []
for graph in graphs:
  vertices_visited = set()
  n_vertex, n_edge = graph.pop(0)
  
  for i in range(n_edge):
    print(i, n_edge, end='\r')
    is_all_connected, min_pos = is_graph_all_connected(graph, n_vertex, vertices_visited, i)

    if is_all_connected == 1:
      is_all_connected_list.append(min_pos)
      break
    else:
      is_all_connected, min_pos = is_graph_all_connected(graph, n_vertex, vertices_visited, i)
  else:
    is_all_connected_list.append(-1)
    
  print(is_all_connected)
  

print(' '.join(map(str, is_all_connected_list)))
  