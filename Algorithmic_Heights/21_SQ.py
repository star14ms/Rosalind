# hard
from util import get_data

data = get_data(__file__)
# data = '''2

# 4 5
# 3 4
# 4 2
# 3 2
# 3 1
# 1 2

# 4 4
# 1 2
# 3 4
# 2 4
# 4 1'''

graphs = data.split('\n\n')[1:]
graphs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), graphs))

def has_square_cycle(graph):
  n_vertices, n_edges = graph.pop(0)
  n = n_vertices
  adj_matrix = [[0] * n for _ in range(n)]
  
  for edge in graph:
    u, v = edge
    adj_matrix[u-1][v-1] = 1

  # import numpy as np
  # print(np.array(adj_matrix))
  
  for i in range(n):
    for j in range(i, n):
      if adj_matrix[i][j] == 1:
        for k in range(j, n):
          if adj_matrix[k][j] == 1:
            for l in range(n):
              if adj_matrix[l][k] == 1 and adj_matrix[l][i] == 1 and i != k:
                return 1

  return -1


print(' '.join(map(str, list(map(has_square_cycle, graphs)))))