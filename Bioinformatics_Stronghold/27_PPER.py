from util import get_data

data = get_data(__file__)
n, k = map(int, data.split())

def permutations(n, k):
    if k == 0:
        return 1
    return n * permutations(n-1, k-1)
  
n_permutations = permutations(n, k)

print(n_permutations % 1_000_000)