from util import get_data, get_output_path
from itertools import product
from _28_BA3F import read_Eulerian_directed_graph, Eulerian_cycle


def construct_DeBruijn_graph_of_every_possible_k_mers(k):
    k_mers = list(map(''.join, product('01', repeat=k)))
    k_mer_to_id = {k_mer: i for i, k_mer in enumerate(k_mers)}

    graph = []
    for k_mer1 in k_mers:
        for k_mer2 in k_mers:
            if k_mer1 != k_mer2 and k_mer1[1:] == k_mer2[:-1]:
                if len(graph) < k_mer_to_id[k_mer1] + 1:
                    graph.append(f"{k_mer_to_id[k_mer1]} -> {k_mer_to_id[k_mer2]}")
                else:
                    graph[k_mer_to_id[k_mer1]] += f",{k_mer_to_id[k_mer2]}"
                # if len(graph) < k_mer_to_id[k_mer1] + 1:
                #     graph.append(f"{k_mer1} -> {k_mer2}")
                # else:
                #     graph[k_mer_to_id[k_mer1]] += f",{k_mer2}"
        
    # print(*graph, sep='\n')
    # breakpoint()
    return sorted(graph)


def build_universal_circular_string(cycle, k):
    k_mers = list(map(''.join, product('01', repeat=k)))
    id_to_kmer = {i: k_mer for i, k_mer in enumerate(k_mers)}
    
    len_edge = len(cycle) + 1
    len_circular = 2 ** k
    len_cycle_to_remove = len_edge - 1 - len_circular
    
    text = id_to_kmer[cycle.pop(0)]
    for node in cycle[:-k]:
        text += id_to_kmer[node][-1]
    
    # print(cycle)
    possible_texts = []
    for id in set(cycle):
        if cycle.count(id) < 2:
            continue

        idx = cycle.index(id)
        while cycle[idx+1:].count(id) > 0:
            idx2 = cycle.index(id, idx+1)
            # print(idx2-idx)
            if idx2 != -1 and idx2 - idx == len_cycle_to_remove:
                possible_texts.append(text[:idx] + text[idx2:])
                break
            else:
                idx = idx2
    # print(possible_texts)
    # breakpoint()
    return text


if __name__ == "__main__":
    # data = get_data(__file__)
    data ='''4'''

    k = int(data)
    graph = construct_DeBruijn_graph_of_every_possible_k_mers(k)
    
    # _28_BA3F.py
    graph = read_Eulerian_directed_graph(graph)
    cycle = Eulerian_cycle(graph)

    k_universal_circular_string = build_universal_circular_string(cycle, k)
    
    with open(get_output_path(__file__), "w") as f:
        print(k_universal_circular_string)
    #     print(k_universal_circular_string, file=f)
