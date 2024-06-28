from util import get_data, get_output_path
# from _28_BA3F import read_Eulerian_directed_graph


def read_Eulerian_directed_path(graph):
    nodes = {}
    for edge in graph:
        edge1, edges2 = edge.split(' -> ')
        edges2 = list(map(int, edges2.split(',')))
        nodes[int(edge1)] = edges2
        
        for edge2 in edges2:
            if edge2 not in nodes:
                nodes[edge2] = []

    return nodes


def get_start_node(graph):
    out_degree = {key: len(value) for key, value in graph.items()}
    in_degree = {key: 0 for key in graph.keys()}

    for outs in graph.values():
        for out in outs:
            in_degree[out] = in_degree.get(out, 0) + 1

    for i in range(len(graph)):
        if i in out_degree and in_degree[i] < out_degree[i]:
            return i

    return 0


def Eulerian_path(graph, start=0):
    current = start
    pathway = [current]
    cycles = []
    non_cycle = None
    branches = set()
    # print(sum([len(node[1]) for node in graph]))

    while any([value for value in graph.values()]): # False in visited or len(branches) > 0:
        if current not in graph or len(graph[current]) == 0:
            non_cycle = pathway.copy()
            current = branches.pop()
            pathway = [current]
            continue

        len_current_branch = len(graph[current])
        
        if len_current_branch == 1 and current in branches:
            branches.remove(current)
        elif len_current_branch >= 2:
            branches.add(current)

        next = graph[current].pop()

        if next == pathway[0]:
            cycles.append(pathway + [next])
            if len(branches) == 0:
                break
            current = branches.pop()
            pathway = [current]
        else:
            current = next
            pathway.append(current)

    while len(cycles) > 0:
        small_cycle = cycles.pop(0)
        index = non_cycle.index(small_cycle[0])
        if index == -1:
            cycles.append(small_cycle)
            continue
        non_cycle = non_cycle[:index] + small_cycle + non_cycle[index+1:]

    # print(len(non_cycle))
    return non_cycle


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''0 -> 2
# 1 -> 3
# 2 -> 1
# 3 -> 0,4
# 6 -> 3,7
# 7 -> 8
# 8 -> 9
# 9 -> 6'''

    graph = data.split('\n')
    
    graph = read_Eulerian_directed_path(graph)
    start = get_start_node(graph)
    cycle = Eulerian_path(graph, start)

    with open(get_output_path(__file__), "w") as f:
        print(*cycle, sep='->')
        print(*cycle, sep='->', file=f)
