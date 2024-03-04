from util import get_data, factorial

data = get_data(__file__)
rna = data.split('\n')[1]

count_a = data.count('A')
count_c = data.count('C')

print(count_a, count_c)

n_au_matching = factorial(count_a)
n_cg_matching = factorial(count_c)

perfect_matchings = n_au_matching * n_cg_matching

print(perfect_matchings)