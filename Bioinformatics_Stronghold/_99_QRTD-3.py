from util import get_data
import numpy as np
from math import comb
from Bio import Phylo
from io import StringIO

from _56_CTBL import solve_newick_problem


def get_n_common_quartets(tree1, tree2):
    is_root_node = getattr(getattr(tree1, 'clade', None), 'clades', None) is not None and len(tree1.clade.clades) == 3

    if is_root_node:
        tree1_clades = tree1.clade.clades
        tree2_clades = tree2.clade.clades
        tree1_0s = set(leaf.name for leaf in tree1_clades[0].get_terminals())
        tree1_1s = set(leaf.name for leaf in tree1_clades[1].get_terminals() + tree1_clades[2].get_terminals())
        tree2_0s = set(leaf.name for leaf in tree2_clades[0].get_terminals())
        tree2_1s = set(leaf.name for leaf in tree2_clades[1].get_terminals() + tree2_clades[2].get_terminals())
    else:
        tree1_clades = tree1.clades
        tree2_clades = tree2.clades
        tree1_0s = set(leaf.name for leaf in tree1_clades[0].get_terminals())
        tree1_1s = set(leaf.name for leaf in tree1_clades[1].get_terminals())
        tree2_0s = set(leaf.name for leaf in tree2_clades[0].get_terminals())
        tree2_1s = set(leaf.name for leaf in tree2_clades[1].get_terminals())

    n_changed_0 = len(tree1_0s ^ tree2_0s)
    n_changed_1 = len(tree1_1s ^ tree2_1s)
    n_constant_0 = len(tree1_0s & tree2_0s)
    n_constant_1 = len(tree1_1s & tree2_1s)

    # 1. {0, 0}, {1, 1}
    # 2. {0', 0'}, {1', 1'}
    n_common_quartets = comb(n_constant_0, 2) * comb(n_constant_1, 2) + \
                        comb(n_changed_0, 2) * comb(n_changed_1, 2)
                        
    if not tree1_clades[0].is_terminal() and not tree2_clades[0].is_terminal():
        n_common_quartets += get_n_common_quartets(tree1_clades[0], tree2_clades[0])
    if is_root_node:
        tree1.clade.clades = tree1.clade.clades[1:]
        tree2.clade.clades = tree2.clade.clades[1:]
        n_common_quartets += get_n_common_quartets(tree1.clade, tree2.clade)
    elif not tree1_clades[1].is_terminal() and not tree2_clades[1].is_terminal():
            n_common_quartets += get_n_common_quartets(tree1_clades[1], tree2_clades[1])

    return n_common_quartets


if __name__ == '__main__':
    # data = get_data(__file__)
    data = '''A B C D E
(A,C,((B,D),E));
(C,(B,D),(A,E));'''

    data = data.split('\n')
    n_taxon = len(data[0].split())
    tree1 = data[1]
    tree2 = data[2]

    character_table1 = np.array([list(map(int, row)) for row in solve_newick_problem(tree1)[:-1]])
    character_table2 = np.array([list(map(int, row)) for row in solve_newick_problem(tree2)[:-1]])
    
    tree1 = Phylo.read(StringIO(tree1), "newick")
    tree2 = Phylo.read(StringIO(tree2), "newick")
    
    n_common_quartets = get_n_common_quartets(tree1, tree2)
    quartet_distance = 2*comb(n_taxon, 4) - 2*n_common_quartets

    print(comb(n_taxon, 4), n_common_quartets)
    print(quartet_distance)



    #     tree1_2s = set(leaf.name for leaf in tree1_clades[2].get_terminals())
    #     tree2_2s = set(leaf.name for leaf in tree2_clades[2].get_terminals())
        
    #     n_changed_0 = len(tree1_0s ^ tree2_0s)
    #     n_constant_0 = len(tree1_0s & tree2_0s)
    #     n_changed_1 = len((tree1_1s | tree1_2s) ^ (tree2_1s | tree2_2s))
    #     n_constant_1 = len((tree1_1s | tree1_2s) & (tree2_1s | tree2_2s))
        
    #     n_common_quartets += comb(n_constant_0, 2) * comb(n_constant_1, 2) + \
    #                     comb(n_changed_0, 2) * comb(n_changed_1, 2)

    #     n_changed_0 = len(tree1_1s ^ tree2_1s)
    #     n_constant_0 = len(tree1_1s & tree2_1s)
    #     n_changed_1 = len((tree1_0s | tree1_2s) ^ (tree2_0s | tree2_2s))
    #     n_constant_1 = len((tree1_0s | tree1_2s) & (tree2_0s | tree2_2s))
        
    #     n_common_quartets += comb(n_constant_0, 2) * comb(n_constant_1, 2) + \
    #                     comb(n_changed_0, 2) * comb(n_changed_1, 2)
                        
    #     n_changed_0 = len(tree1_2s ^ tree2_2s)
    #     n_constant_0 = len(tree1_2s & tree2_2s)
    #     n_changed_1 = len((tree1_0s | tree1_1s) ^ (tree2_0s | tree2_1s))
    #     n_constant_1 = len((tree1_1s | tree1_2s) & (tree2_1s | tree2_2s))
        
    #     n_common_quartets += comb(n_constant_0, 2) * comb(n_constant_1, 2) + \
    #                     comb(n_changed_0, 2) * comb(n_changed_1, 2)
        
    #     # 1. {0, 0}, {1, 1} 1*1
    #     # 2. {2, 2}, {0, 0} 1*1
    #     # 3. {2, 2}, {1, 1} 1*1
    #     # 4. {0, 0}, {1, 2} 2*2
    #     # 5. {1, 1}, {0, 2} 2*2
    #     # 6. {2, 2}, {0, 1} 2*2
        
    #     # n_common_quartets += comb(n_constant_2, 2) * comb(n_constant_0, 2) + \
    #     #                     comb(n_constant_2, 2) * comb(n_constant_1, 2) + \
    #     #                     comb(n_constant_0, 2) * comb(n_constant_1, 1) * comb(n_constant_2, 1) + \
    #     #                     comb(n_constant_1, 2) * comb(n_constant_0, 1) * comb(n_constant_2, 1) + \
    #     #                     comb(n_constant_2, 2) * comb(n_constant_0, 1) * comb(n_constant_1, 1) + \
    #     #                     comb(n_changed_2, 2) * comb(n_changed_0, 2) + \
    #     #                     comb(n_changed_2, 2) * comb(n_changed_1, 2) + \
    #     #                     comb(n_changed_0, 2) * comb(n_changed_1, 1) * comb(n_changed_2, 1) + \
    #     #                     comb(n_changed_1, 2) * comb(n_changed_0, 1) * comb(n_changed_2, 1) + \
    #     #                     comb(n_changed_2, 2) * comb(n_changed_0, 1) * comb(n_changed_1, 1)
    