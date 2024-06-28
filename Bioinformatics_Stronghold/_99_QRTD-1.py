### Too much time to solve this problem. I need to find a better solution.
from util import get_data
from _56_CTBL import solve_newick_problem
from _72_QRT import get_quartets


if __name__ == '__main__':
    # data = get_data(__file__)
    data = '''A B C D E
(A,C,((B,D),E));
(C,(B,D),(A,E));'''

    data = data.split('\n')
    taxon = data[0].split()
    tree1 = data[1]
    tree2 = data[2]

    character_table1 = [''.join(row) for row in solve_newick_problem(tree1)[:-1]]
    character_table2 = [''.join(row) for row in solve_newick_problem(tree2)[:-1]]

    quartets1, _ = get_quartets(character_table1, taxon)
    quartets2, _ = get_quartets(character_table2, taxon)

    quartets1 = set([''.join(sorted(map(str, split1)) + sorted(map(str, split2))) for (split1, split2) in quartets1])
    quartets2 = set([''.join(sorted(map(str, split1)) + sorted(map(str, split2))) for (split1, split2) in quartets2])

    quartet_distance = len(quartets1 ^ quartets2)
    print(quartet_distance)
