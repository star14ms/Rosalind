from util import get_data

data = get_data(__file__)

graphs = data.split('\n\n')[1:]
graphs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), graphs))

def is_bipartite(graph):
  # graph: [[v, n], [a, b], [c, d], ...
  n_vertices = graph.pop(0)[0]
  color = [-1] * n_vertices
  offset = 0
  color[offset] = 0
  queue = [offset]

  while queue:
    u = queue.pop(0)
    
    for node in list(filter(lambda x: x[0] == u+1 or x[1] == u+1, graph)):
      for v in node:
        if v-1 == u:
          continue
        if color[v-1] == -1:
          color[v-1] = 1 - color[u]
          queue.append(v-1)
        elif color[v-1] == color[u]:
          return -1
  return 1

bipartite_list = list(map(is_bipartite, graphs))

with open('Algorithmic_Heights/output/15_BIP.txt', 'w') as f:
  f.write(' '.join(map(str, bipartite_list)))