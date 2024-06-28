from util import get_data, get_output_path


def construct_overlap_graph(k_mers):
    graph = []
    while k_mers:
        k_mer = k_mers.pop(0)
        for k_mer2 in k_mers:
            if k_mer[1:] == k_mer2[:-1]:
                graph.append(f"{k_mer} -> {k_mer2}")
            if k_mer2[1:] == k_mer[:-1]:
                graph.append(f"{k_mer2} -> {k_mer}")
                
    return '\n'.join(graph)


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''ATGCG
# GCATG
# CATGC
# AGGCA
# GGCAT'''

    kmers = data.split('\n')
    graph = construct_overlap_graph(kmers)

    with open(get_output_path(__file__), "w") as f:
        print(graph, sep='\n')
        print(graph, sep='\n', file=f)
