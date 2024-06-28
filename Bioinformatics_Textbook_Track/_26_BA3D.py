from util import get_data, get_output_path
from collections import defaultdict


# def construct_DeBruijn_graph_of_string(text, k):
#     graph = []
#     for i in range(len(text) - k + 1):
#         k_mer = text[i:i+k]
#         idx_kmer_node = list(filter(lambda i: graph[i][:k-1] == k_mer[:-1], range(len(graph))))
#         if len(idx_kmer_node) == 0:
#             graph.append(f"{k_mer[:-1]} -> {k_mer[1:]}")
#         else:
#             graph[idx_kmer_node[0]] += f",{k_mer[1:]}"
            
#     return sorted(graph)


def de_bruijn_graph_of_string(text, k, stringified=False):
    graph = defaultdict(list)
    for i in range(len(text) - k + 1):
        graph[text[i:i+k-1]].append(text[i+1:i+k])
    return sorted([f"{k} -> {','.join(v)}" for k, v in graph.items()]) if stringified else graph


if __name__ == "__main__":
    # data = get_data(__file__)
    data ='''4
AAGATTCTCTAC'''

    k, text = data.split('\n')
    # graph = construct_DeBruijn_graph_of_string(text, int(k))
    graph = de_bruijn_graph_of_string(text, int(k), stringified=True)

    with open(get_output_path(__file__), "w") as f:
        print(*graph, sep='\n')
        print(*graph, sep='\n', file=f)
