from util import get_data, factorial

data = get_data(__file__)

# data = '''6
# (lobster,(cat,dog),(caterpillar,(elephant,mouse)));'''


def number_of_leaves(tree):
    return tree.count(',') + 1
  
def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


n_quartets = int(choose(number_of_leaves(data), 4))

print(n_quartets % 1000000)
