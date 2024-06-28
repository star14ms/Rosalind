from util import get_data, get_output_path
from _29_BA3G import read_Eulerian_directed_path
from collections import defaultdict


def construct_reversed_graph(graph):
    reversed_graph = defaultdict(list)
    for key, value in graph.items():
        for node in value:
            reversed_graph[node].append(key)
            
            if node not in reversed_graph:
                reversed_graph[node] = []

    return reversed_graph


def MaximalNonBranchingPaths(graph):
    graph_reversed = construct_reversed_graph(graph)
    paths = []
    asolated_cycles = []
    for node_in, nodes_out in graph.items():
        if len(nodes_out) != 1 or len(graph_reversed[node_in]) != 1:
            if len(nodes_out) > 0:
                for node in nodes_out:
                    non_branching_path = [node_in, node]
                    while len(graph[node]) == 1 and len(graph_reversed[node]) == 1:
                        node = graph[node][0]
                        non_branching_path.append(node)
                    paths.append(non_branching_path)

        elif not any([node_in in asolated_cycle for asolated_cycle in asolated_cycles]):
            cycle = [node_in, nodes_out[0]]
            while True:
                if len(graph[cycle[-1]]) != 1 or len(graph_reversed[graph[cycle[-1]][0]]) != 1:
                    break

                node = graph[cycle[-1]][0]
                if node == node_in:
                    asolated_cycles.append(cycle + [node_in])
                    break
                cycle.append(node)
                   
    return paths + asolated_cycles


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''1 -> 2
# 2 -> 3
# 3 -> 4,5
# 6 -> 7
# 7 -> 6'''

    graph = data.split('\n')
    
    graph = read_Eulerian_directed_path(graph)
    paths = MaximalNonBranchingPaths(graph)

    with open(get_output_path(__file__), "w") as f:
        for path in paths:
            print(' -> '.join(map(str, path)))
            print(' -> '.join(map(str, path)), file=f)
