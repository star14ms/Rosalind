### hard
from util import get_data
import numpy as np

data = get_data('42_REAR.py')
# data = '''1 2 3 4 5 6 7 8 9 10
# 3 1 5 2 7 4 9 6 10 8

# 3 10 8 2 5 4 7 1 6 9
# 5 2 3 1 7 4 10 8 6 9

# 8 6 7 9 4 1 3 10 2 5
# 8 2 7 6 9 1 5 3 10 4

# 3 9 10 4 1 8 6 7 5 2
# 2 9 8 5 1 7 3 4 6 10

# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10

# 9 1 3 2 8 5 4 10 7 6
# 9 3 5 8 1 10 7 4 2 6'''
data = data.split('\n\n')
pairs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), data))


def best_intersection(P, Q):
  for perm in P:
    if perm in Q:
      return P[perm] + Q[perm]
  return -1

def make_step(processed, border, next_border):
  for perm in border:
    for j in range(len(perm)+1):
      for i in range(j-1): # at least 2 numbers reversed
        new_perm = perm[:i] + perm[i:j][::-1] + perm[j:]  # reverse [i,j]

        if new_perm not in processed and new_perm not in border:
          next_border[new_perm] = border[perm] + 1

  processed.update(border)
  border.clear()
  border.update(next_border)
  next_border.clear()

def rev_dist(perm1, perm2):
  processed1 = {}
  border1 = {}
  next_border1 = {}

  processed2 = {}
  border2 = {}
  next_border2 = {}

  border1[tuple(perm1)] = 0
  border2[tuple(perm2)] = 0

  lamp = False
  while best_intersection(border1, border2) == -1:
    if lamp:
      make_step(processed1, border1, next_border1)
    else:
      make_step(processed2, border2, next_border2)
    lamp = not lamp

  return best_intersection(border1, border2)

for pair1, pair2 in pairs:
  print(rev_dist(pair1, pair2), end=' ')