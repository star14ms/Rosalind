from util import get_data, get_output_path
from collections import defaultdict


def generate_contigs(k_mers):
    graph_next = defaultdict(list)
    for k_mer1 in k_mers:
        for k_mer2 in k_mers: 
            if k_mer1[1:] == k_mer2[:-1]:
                graph_next[k_mer1].append(k_mer2)

    graph_prev = defaultdict(list)
    for k_mer1 in k_mers:
        for k_mer2 in k_mers: 
            if k_mer1[:-1] == k_mer2[1:]:
                graph_prev[k_mer1].append(k_mer2)
    
    k = len(k_mers[0])
    in1_k_mers = {key: value[0] for key, value in graph_next.items() if len(value) == 1}
    out1_k_mers = {key: value[0] for key, value in graph_prev.items() if len(value) == 1}
    
    contigs = []
    while k_mers:
        contig = k_mers.pop(0)
        
        if contig not in in1_k_mers and contig not in out1_k_mers:
            contigs.append(contig)
            continue
        
        while True:
            k_mer_in = contig[-k:]
            k_mer_out = contig[:k]
            if k_mer_in in in1_k_mers and in1_k_mers[k_mer_in] in out1_k_mers:
                contig = contig + in1_k_mers[k_mer_in][-1]
                k_mers.remove(in1_k_mers[k_mer_in])
            elif k_mer_out in out1_k_mers and out1_k_mers[k_mer_out] in in1_k_mers:
                contig = out1_k_mers[k_mer_out][0] + contig
                k_mers.remove(out1_k_mers[k_mer_out])
            else:
                contigs.append(contig)
                break

    return contigs


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''ATG
# ATG
# TGT
# TGG
# CAT
# GGA
# GAT
# AGA'''

    k_mers = data.split('\n')
    
    contigs = generate_contigs(k_mers)
    
    with open(get_output_path(__file__), "w") as f:
        print(*contigs)
        print(*contigs, file=f)
