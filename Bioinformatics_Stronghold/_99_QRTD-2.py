from util import get_data
import numpy as np
from math import comb

from _56_CTBL import solve_newick_problem
from _72_QRT import get_quartets


if __name__ == '__main__':
    data = get_data('100_QRTD.py')
#     data = '''A B C D E
# (A,C,((B,D),E));
# (C,(B,D),(A,E));'''

    data = data.split('\n')
    n_taxon = len(data[0].split())
    tree1 = data[1]
    tree2 = data[2]

    character_table1 = np.array([list(map(int, row)) for row in solve_newick_problem(tree1)[:-1]])
    character_table2 = np.array([list(map(int, row)) for row in solve_newick_problem(tree2)[:-1]])

    n_common_quartets = 0

    for row1, row2 in zip(character_table1, character_table2):
        idxs_changed = np.where(row1 != row2)[0]
        idxs_constant = np.where(row1 == row2)[0]

        n_0_changed = 0
        n_1_changed = 0
        for idx_changed in idxs_changed:
            if row2[idx_changed] == 0:
                n_0_changed += 1
            else:
                n_1_changed += 1

        n_0_constant = 0
        n_1_constant = 0
        for idx_constant in idxs_constant:
            if row2[idx_constant] == 0:
                n_0_constant += 1
            else:
                n_1_constant += 1
        
        # 1. {0, 0}, {1, 1}
        # 2. {0', 0'}, {1', 1'}
        n_common_quartets += comb(n_0_constant, 2) * comb(n_1_constant, 2) + \
                            comb(n_0_changed, 2) * comb(n_1_changed, 2)
    
    quartet_distance = 2*comb(n_taxon, 4) - 2*n_common_quartets
    print(quartet_distance)
