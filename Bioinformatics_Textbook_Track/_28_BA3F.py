### hard
from util import get_data, get_output_path


def read_Eulerian_directed_graph(graph):
    nodes = []
    for edge in graph:
        edge1, edge2 = edge.split(' -> ')
        edge2 = list(map(int, edge2.split(',')))
        nodes.append((int(edge1), edge2))

    return sorted(nodes, key=lambda x: x[0])


def Eulerian_cycle(graph):
    current = 0
    pathway = [current]
    cycles = []
    branches = set()
    # print(sum([len(node[1]) for node in graph]))

    while any([node[1] for node in graph]):
        # print(len(pathway), graph[current])
        len_current_branch = len(graph[current][1])
        
        if len_current_branch == 1 and current in branches:
            branches.remove(current)
        elif len_current_branch >= 2:
            branches.add(current)

        next = graph[current][1].pop()

        if next == pathway[0]:
            cycles.append(pathway + [next])
            if len(branches) == 0:
                break
            current = branches.pop()
            pathway = [current]
        else:
            current = next
            pathway.append(current)
    
    idx_longest_cycle = max(range(len(cycles)), key=lambda i: len(cycles[i]))
    merged_cycle = cycles.pop(idx_longest_cycle)

    while len(cycles) > 0:
        small_cycle = cycles.pop(0)
        index = merged_cycle.index(small_cycle[0])
        if index == -1:
            cycles.append(small_cycle)
            continue
        merged_cycle = merged_cycle[:index] + small_cycle + merged_cycle[index+1:]

    # print(len(merged_cycle))
    return merged_cycle


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''0 -> 3
# 1 -> 0
# 2 -> 1,6
# 3 -> 2
# 4 -> 2
# 5 -> 4
# 6 -> 5,8
# 7 -> 9
# 8 -> 7
# 9 -> 6'''

    graph = data.split('\n')
    
    graph = read_Eulerian_directed_graph(graph)
    cycle = Eulerian_cycle(graph)

    with open(get_output_path(__file__), "w") as f:
        # print(*cycle, sep='->')
        print(*cycle, sep='->', file=f)
