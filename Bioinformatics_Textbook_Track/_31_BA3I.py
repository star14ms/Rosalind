### ChatGPT: https://chatgpt.com/share/75804454-edb5-494e-b863-0967ece73de2
from util import get_data, get_output_path
from collections import defaultdict, deque

def de_bruijn_graph(k):
    """Generates the De Bruijn graph for the binary alphabet {0, 1} and order k."""
    nodes = [bin(i)[2:].zfill(k) for i in range(2**k)]
    graph = defaultdict(list)
    for node in nodes:
        graph[node[:-1]].append(node[1:])
    return graph

def find_eulerian_cycle(graph):
    """Finds an Eulerian cycle in the given graph."""
    # Start from a node which has outgoing edges
    start_node = next(node for node, edges in graph.items() if edges)
    stack = [start_node]
    cycle = []
    # Current path of the cycle
    current_path = []

    while stack:
        vertex = stack[-1]
        if graph[vertex]:
            next_vertex = graph[vertex].pop()
            stack.append(next_vertex)
        else:
            cycle.append(stack.pop())

    return cycle[::-1]

def k_universal_circular_binary_string(k):
    """Generates a k-universal circular binary string."""
    graph = de_bruijn_graph(k)
    cycle = find_eulerian_cycle(graph)
    # Construct the string from the cycle
    # Start from the second character of each node in the cycle, since the first overlaps
    return ''.join(node[-1] for node in cycle[:-1])  # omit the last to avoid duplication


if __name__ == "__main__":
    data = get_data(__file__)
    # data ='''4'''
    k = int(data)

    text = k_universal_circular_binary_string(k)

    with open(get_output_path(__file__), "w") as f:
        print(text)
        print(text, file=f)
