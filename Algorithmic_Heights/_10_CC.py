from util import get_data

data = get_data(__file__)

data = data.split('\n')
vertex_count, edge_count = map(int, data[0].split())
edges = [tuple(map(int, edge.split())) for edge in data[1:]]

connected_components = [{*edges.pop(0)}]
len_edges = len(edges)

while edges:
  for edge in edges[:]:
      for connected_component in connected_components:
          if edge[0] in connected_component or edge[1] in connected_component:
              connected_component.add(edge[0])
              connected_component.add(edge[1])
              edges.remove(edge)
              break

  if len_edges == len(edges):
    connected_components.append({*edges.pop(0)})
  len_edges = len(edges)
  
for i in range(1, vertex_count+1):
  for connected_component in connected_components:
      if i in connected_component:
          break
  else:
      connected_components.append({i})

print(connected_components)
print(len(connected_components))
