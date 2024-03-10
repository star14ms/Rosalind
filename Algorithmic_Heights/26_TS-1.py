from util import get_data

data = get_data("26_TS.py")
# data = '''4 5
# 1 2
# 3 1
# 3 2
# 4 3
# 4 2'''

graph = [list(map(int, x.split())) for x in data.split('\n')]

# def topology_sort(graph):
#   sorted_graph = [graph[0][0], graph[0][1]]

#   for node in graph:
#     if node[0] == sorted_graph[-1]:
#       sorted_graph.append(node[1])
#     elif node[1] == sorted_graph[0]:
#       sorted_graph.insert(0, node[0])

#   return sorted_graph
  
# but this is not a complete solution, it only works for this specific case
# and it's not even a topological sort, it's just a sort
# I need to find a way to implement a topological sort algorithm
# I will try to implement a DFS algorithm and see if it works
# I will also try to implement a BFS algorithm and see if it works
# I will also try to implement a Kahn's algorithm and see if it works

# DFS
# def topology_sort(graph):
#   visited = [False] * (len(graph) + 1)
#   stack = []
#   sorted_graph = []

#   for node in graph:
#     if not visited[node[0]]:
#       stack.append(node[0])
#       visited[node[0]] = True
#       while stack:
#         current_node = stack.pop()
#         sorted_graph.append(current_node)
#         for neighbor in graph:
#           if neighbor[0] == current_node and not visited[neighbor[1]]:
#             stack.append(neighbor[1])
#             visited[neighbor[1]] = True

#   return sorted_graph[::-1]


def longest_line(graph, n_vertex, n_nodes, offset=0):
  pos_graph = [None] * n_nodes
  pos_graph[offset] = 0
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
        pos_graph[graph.index(node)] = pos[now] + 1
        queue.append(next)
        
  # left
  queue = [graph[offset][0]-1]
  while queue:
    now = queue.pop(0)
    for node in filter(lambda x: x[1]-1 == now and graph.index(x) != offset, graph):
      next = node[0]-1
      if pos[next] == None or pos[next] < pos[now] - 1:
        pos[next] = pos[now] - 1
        pos_graph[graph.index(node)] = pos[now] - 1
        queue.append(next)

  # right
  max_positon = max(filter(lambda x: x != None, pos_graph))
  right_sorted_graph = [graph[pos_graph.index(max_positon)][1]]

  for cursor in range(max_positon, 1, -1):
    i = list(filter(
      lambda i: pos_graph[i] == cursor and right_sorted_graph[0] == graph[i][1], 
      range(len(pos_graph))
    ))[0]

    next_vertex = graph[i][0]
    right_sorted_graph.insert(0, next_vertex)

  # left
  min_positon = min(filter(lambda x: x != None, pos_graph))
  left_sorted_graph = [graph[pos_graph.index(min_positon)][0]]

  for cursor in range(min_positon, 1, 1):
    i = list(filter(
      lambda i: pos_graph[i] == cursor and left_sorted_graph[-1] == graph[i][0], 
      range(len(pos_graph))
    ))[0]

    next_vertex = graph[i][1]
    left_sorted_graph.append(next_vertex)
  
  sorted_graph = left_sorted_graph + right_sorted_graph

  for i in sorted_graph:
    for node in graph:
      if node[0] == i:
        graph.remove(node)
      if node[1] == i:
        graph.remove(node)

  return sorted_graph, graph


longest_graph = []
sorted_graphs = []
n_vertex, n_nodes = graph.pop(0)

while len(graph) > 0:
  sorted_graph, graph = longest_line(graph, n_vertex, n_nodes)
  sorted_graphs.append(sorted_graph)

  if len(sorted_graph) > len(longest_graph):
    longest_graph = sorted_graph
    
print(longest_graph)


# with open('Algorithmic_Heights/output/26_TS.txt', 'w') as output_data:
#     output_data.write(' '.join(map(str, longest_graph)) + '\n')