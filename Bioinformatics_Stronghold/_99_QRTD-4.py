from util import get_data
from math import comb
from Bio import Phylo
from io import StringIO
from tqdm import tqdm

from _56_CTBL import solve_newick_problem


def get_n_common_quartets_from_two_edges(edge1, edge2, tree1, tree2, F1_idx=0, G1_idx=0):
    F1 = set(leaf.name for leaf in tree1.clade.clades[F1_idx].get_terminals())
    F2 = set(leaf.name for leaf in edge1.clades[0 if len(edge1.clades) != 3 else F1_idx-1].get_terminals())
    F3 = set(leaf.name for leaf in edge1.clades[1 if len(edge1.clades) != 3 else F1_idx-2].get_terminals())

    G1 = set(leaf.name for leaf in tree2.clade.clades[G1_idx].get_terminals())
    G2 = set(leaf.name for leaf in edge2.clades[0 if len(edge2.clades) != 3 else G1_idx-1].get_terminals())
    G3 = set(leaf.name for leaf in edge2.clades[1 if len(edge2.clades) != 3 else G1_idx-2].get_terminals())

    n_common_quartets = comb(len(F1 & G1), 2) * (len(F2 & G2) * len(F3 & G3) + len(F2 & G3) * len(G3 & F2))

    return n_common_quartets


def get_n_common_quartets(tree1, tree2):
    n_common_quartets = 0
    tree1_clades = tree1.clade.clades
    tree2_clades = tree2.clade.clades

    for i in range(3):
        for j in range(3):
            for edge1 in tqdm([tree1.clade] + tree1_clades[i-1].get_nonterminals() + tree1_clades[i-2].get_nonterminals()):
                for edge2 in [tree2.clade] + tree2_clades[j-1].get_nonterminals() + tree2_clades[j-2].get_nonterminals():
                    n_common_quartets += get_n_common_quartets_from_two_edges(edge1, edge2, tree1, tree2, i, j)
                    
    return n_common_quartets


if __name__ == '__main__':
    data = get_data(__file__)
#     data = '''A B C D E
# (A,C,((B,D),E));
# (C,(B,D),(A,E));'''

    data = data.split('\n')
    n_taxon = len(data[0].split())
    tree1 = Phylo.read(StringIO(data[1]), "newick")
    tree2 = Phylo.read(StringIO(data[2]), "newick")

    n_common_quartets = get_n_common_quartets(tree1, tree2)

    quartet_distance = comb(n_taxon, 4) - n_common_quartets
    print(comb(n_taxon, 4), n_common_quartets)
    print(quartet_distance)
