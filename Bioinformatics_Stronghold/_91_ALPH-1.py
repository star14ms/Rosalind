from util import get_data
from Bio import Phylo
from io import StringIO


def hamming_distance(seq1, seq2):
    """Calculate the Hamming distance between two sequences."""
    return sum(ch1 != ch2 for ch1, ch2 in zip(seq1, seq2))


if __name__ == '__main__':
    # data = get_data(__file__)
    data = '''(((ostrich,cat)rat,(duck,fly)mouse)dog,(elephant,pikachu)hamster)robot;
>ostrich
AC
>cat
CA
>duck
T-
>fly
GC
>elephant
-T
>pikachu
AA'''

    data = data.split('\n', 1)
    tree = Phylo.read(StringIO(data[0]), "newick")

    multiple_alignment_dict = {}
    for line in data[1].split('>')[1:]:
        name, sequence, *_ = line.split('\n')
        multiple_alignment_dict[name] = sequence

    print(multiple_alignment_dict)

    # (A,B): Hamming distance between A and B

    for leaf in tree.get_nonterminals():
        edges_connected_to_leaf = list(filter(lambda edge: edge[0].name == leaf.name or edge[1].name == leaf.name, list(Phylo.to_networkx(tree).edges)))
        
        are_another_edge_assigned = [
          edge[0].name in multiple_alignment_dict or \
          edge[1].name in multiple_alignment_dict 
            for edge in edges_connected_to_leaf
        ]

        if are_another_edge_assigned.count(False) > 1:
            continue

        dna_strings = []
        for edge in edges_connected_to_leaf:
            if edge[0].name in multiple_alignment_dict:
                dna_strings.append(multiple_alignment_dict[edge[0].name])
            elif edge[1].name in multiple_alignment_dict:
                dna_strings.append(multiple_alignment_dict[edge[1].name])
            else:
                continue

        print(leaf.name, dna_strings)


def assign_dna_to_internal_nodes(tree):
    for node in tree.get_nonterminals():
        edges_connected_to_node = list(filter(lambda edge: edge[0].name == node.name or edge[1].name == node.name, list(Phylo.to_networkx(tree).edges)))
        
        are_another_edge_assigned = [
          edge[0].name in multiple_alignment_dict or \
          edge[1].name in multiple_alignment_dict 
            for edge in edges_connected_to_node
        ]

        if are_another_edge_assigned.count(False) > 1:
            continue

        dna_strings = []
        for edge in edges_connected_to_node:
            if edge[0].name in multiple_alignment_dict:
                dna_strings.append(multiple_alignment_dict[edge[0].name])
            elif edge[1].name in multiple_alignment_dict:
                dna_strings.append(multiple_alignment_dict[edge[1].name])
            else:
                continue

        print(node.name, dna_strings)