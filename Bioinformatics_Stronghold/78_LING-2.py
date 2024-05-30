from util import get_data


dna = get_data(__file__)
# dna = '''ATTTGGATT'''
# dna = '''AAAAAAAAA'''


# SUFF = __import__('75_SUFF')
# get_suffix_tree = SUFF.get_suffix_tree
# print_substrings_of_suffix_tree = SUFF.print_substrings_of_suffix_tree

# suffix_tree = get_suffix_tree(dna)
# print_substrings_of_suffix_tree(suffix_tree)


n_distinct_substrings_total = 0
n_possible_substrings_total = 0

for k in range(1, int(len(dna)**(1/2))):
    k_mer_set = set()
    for i in range(len(dna) - k + 1):
        k_mer_set.add(dna[i:i + k])

    n_possible_substrings = min(4**k, len(dna) - k + 1)

    n_distinct_substrings_total += len(k_mer_set)
    n_possible_substrings_total += n_possible_substrings

    print(k, len(k_mer_set), n_possible_substrings, '%6f' % (n_distinct_substrings_total / n_possible_substrings_total), end='\n' if k < 10 else '\r')
