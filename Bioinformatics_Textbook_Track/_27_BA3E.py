from util import get_data, get_output_path
from collections import defaultdict


# def construct_DeBruijn_graph_of_kmers(k_mers):
#     k = len(k_mers[0])
#     graph = []
#     for k_mer in k_mers:
#         idx_kmer_node = list(filter(lambda i: graph[i][:k-1] == k_mer[:-1], range(len(graph))))
#         if len(idx_kmer_node) == 0:
#             graph.append(f"{k_mer[:-1]} -> {k_mer[1:]}")
#         else:
#             graph[idx_kmer_node[0]] += f",{k_mer[1:]}"
            
#     return sorted(graph)


def de_bruijn_graph_of_kmers(k_mers, stringified=False):
    graph = defaultdict(list)
    for k_mer in k_mers:
        graph[k_mer[:-1]].append(k_mer[1:])
    return sorted([f"{k} -> {','.join(v)}" for k, v in graph.items()]) if stringified else graph


if __name__ == "__main__":
    data = get_data(__file__)
    data ='''GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG'''

    k_mers = data.split('\n')
    graph = de_bruijn_graph_of_kmers(k_mers, stringified=True)

    with open(get_output_path(__file__), "w") as f:
        print(*graph, sep='\n')
        print(*graph, sep='\n', file=f)
