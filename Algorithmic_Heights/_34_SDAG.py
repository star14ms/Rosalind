from util import get_data, get_output_path

data = get_data(__file__)
# data = '''5 6
# 2 3 4
# 4 3 -2
# 1 4 1
# 1 5 -3
# 2 4 -2
# 5 4 1'''
graph = list(map(lambda x: list(map(int, x.split())), data.split('\n')))


def bellman_ford(n, edges, offset=1):
    # Initialize distance array with infinity for all vertices
    # Assuming vertex numbering starts from 1, we adjust the array size accordingly
    dist = [float('inf')] * (n + 1)
    dist[offset] = 0  # Assuming the problem uses 1-indexing and we choose vertex 1 as the starting point

    # Relax edges repeatedly
    for i in range(n-1):
        print(i, end='\r')
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # queue = [offset]
    # while queue:
    #   u = queue.pop(0)
    #   for u, v, w in filter(lambda x: x[0] == u, edges):
    #     if dist[v] > dist[u] + w:
    #       dist[v] = dist[u] + w
    #       if v not in queue:
    #         queue.append(v)

    return dist[1:]


n, m = graph.pop(0)
dist = bellman_ford(n, graph, 1)

answer = ' '.join(map(lambda x: 'x' if x == float('inf') else str(x), dist))
print(answer)

with open(get_output_path(__file__), 'w') as output_data:
    output_data.write(answer + '\n')
