### hard
from util import get_data, get_output_path
import numpy as np


tree = get_data(__file__)
# tree = '''((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa);'''

def contract_tree(tree):
  if tree.count(',') == tree.count('(') == tree.count(')'):
    tree = tree[1:-1]

  if tree in contract_tree.cache:
    return contract_tree.cache[tree]

  start = 0
  middle = tree.find(',')
  while not tree[:middle].count('(') == tree[:middle].count(')'):
    start = middle + 1
    middle = tree.find(',', start)

  left, right = tree[:middle], tree[middle+1:]

  if left not in contract_tree.cache:
    contract_tree(left)
  if right not in contract_tree.cache:
    contract_tree(right)

  left_weight = contract_tree.cache[left]
  right_weight = contract_tree.cache[right]

  prob = \
    (np.array([4, 0, 0]) * left_weight[0] * right_weight[0]) + \
    (np.array([0, 0, 4]) * left_weight[2] * right_weight[2]) + \
    (np.array([0, 4, 0]) * left_weight[0] * right_weight[2]) + \
    (np.array([0, 4, 0]) * left_weight[2] * right_weight[0]) + \
    (np.array([2, 2, 0]) * left_weight[0] * right_weight[1]) + \
    (np.array([2, 2, 0]) * left_weight[1] * right_weight[0]) + \
    (np.array([0, 2, 2]) * left_weight[2] * right_weight[1]) + \
    (np.array([0, 2, 2]) * left_weight[1] * right_weight[2]) + \
    (np.array([1, 2, 1]) * left_weight[1] * right_weight[1])

  contract_tree.cache[f'({left},{right})'] = prob
  return prob


contract_tree.cache = {
  'AA': np.array([1, 0, 0], dtype=np.float64),
  'aa': np.array([0, 0, 1], dtype=np.float64),
  'Aa': np.array([0, 1, 0], dtype=np.float64),
  # '(AA,AA)': np.array([4, 0, 0], dtype=np.float64),
  # '(aa,aa)': np.array([0, 0, 4], dtype=np.float64),
  # '(AA,aa)': np.array([0, 4, 0], dtype=np.float64),
  # '(aa,AA)': np.array([0, 4, 0], dtype=np.float64),
  # '(AA,Aa)': np.array([2, 2, 0], dtype=np.float64),
  # '(Aa,AA)': np.array([2, 2, 0], dtype=np.float64),
  # '(aa,Aa)': np.array([0, 2, 2], dtype=np.float64),
  # '(Aa,aa)': np.array([0, 2, 2], dtype=np.float64),
  # '(Aa,Aa)': np.array([1, 2, 1], dtype=np.float64),
}

probs = contract_tree(tree.rstrip(';'))
total = probs.sum()

print(len(contract_tree.cache))
print(*np.round(probs / total, 3).tolist())
