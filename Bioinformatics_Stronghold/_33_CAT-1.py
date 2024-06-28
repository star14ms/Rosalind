### hard
from util import get_data
import re
import sys
sys.setrecursionlimit(1000)

data = get_data('33_CAT.py')
# data ='''>Rosalind_57
# AUAU'''
rna = data.split('\n')[1]


def catalan(n):
  if n <= len(catalan_numbers):
    return catalan_numbers[n - 1]
  if n == 1:
    return 1
  return sum([catalan(i) * catalan(n - i) for i in range(1, n)]) # if print(i, n-i) or True

catalan_numbers = []
for i in range(1, len(rna)):
  catalan_numbers.append(catalan(i))

# AU_count = catalan(rna.count('A') + 1)
# GC_count = catalan(rna.count('G') + 1)
# print(AU_count * GC_count)


def get_base_indexes(seq):
  base_indexes = {}

  for base in ['A', 'U', 'G', 'C']:
    finditer = re.finditer(base, seq)
    finditer = list(map(lambda iter: iter.span()[0] + 1, finditer))
    
    base_indexes[base] = finditer
  return base_indexes


complement = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}


def get_n_non_crossing_from_6_bases(seq):
    n_non_crossing = 0
    if len(seq) == 2:
      if seq[0] == complement[seq[1]]:
        n_non_crossing += 1
    elif len(seq) == 4:
      if seq[0] == complement[seq[1]] and seq[2] == complement[seq[3]]:
        n_non_crossing += 1
      if seq[1] == complement[seq[2]] and seq[3] == complement[seq[0]]:
        n_non_crossing += 1
    elif len(seq) == 6:
      if seq[0] == complement[seq[1]] and seq[2] == complement[seq[3]] and seq[4] == complement[seq[5]]:
        n_non_crossing += 1
      if seq[1] == complement[seq[2]] and seq[3] == complement[seq[4]] and seq[5] == complement[seq[0]]:
        n_non_crossing += 1
      if seq[0] == complement[seq[1]] and seq[2] == complement[seq[5]] and seq[3] == complement[seq[4]]:
        n_non_crossing += 1
      if seq[0] == complement[seq[3]] and seq[1] == complement[seq[2]] and seq[4] == complement[seq[5]]:
        n_non_crossing += 1
      if seq[0] == complement[seq[5]] and seq[1] == complement[seq[4]] and seq[2] == complement[seq[3]]:
        n_non_crossing += 1
    
    return n_non_crossing


def get_possible_pairs(seq):
  base_indexes = get_base_indexes(seq)
  possible_pairs = []

  for A_index in base_indexes['A']:
    for U_index in base_indexes['U']:
      left, right = (A_index, U_index) if A_index < U_index else (U_index, A_index)
      period1 = seq[left+1:right]
      period2 = seq[right+1:] + seq[:left]
      
      if period1.count('A') != period1.count('U') or \
        period1.count('G') != period1.count('C'):
        continue
      
      possible_pairs.append([(left, right), period1, period2])

  for G_index in base_indexes['G']:
    for C_index in base_indexes['C']:
      left, right = (G_index, C_index) if G_index < C_index else (C_index, G_index)
      period1 = seq[left+1:right]
      period2 = seq[right+1:] + seq[:left]
      
      if period1.count('A') != period1.count('U') or \
        period1.count('G') != period1.count('C'):
          continue
        
      possible_pairs.append([(left, right), period1, period2])
      
  return possible_pairs


def get_n_non_crossing(seq):
  base_indexes = get_base_indexes(seq)
  
  n_non_crossing = 0
  
  for A_index in base_indexes['A']:
    for U_index in base_indexes['U']:
      if A_index < U_index:
        left, right = A_index, U_index
      else:
        left, right = U_index, A_index
        
      if (right - left) <= 2 or len(seq) - right <= 2:
        continue
        
      period1 = seq[left+1:right]
      period2 = seq[right+1:] + seq[:left]
      
      if period1.count('A') != period1.count('U') or \
        period1.count('G') != period1.count('C'): # (right - left) % 2 == 0
        continue
      
      if len(period1) <= 6:
        n_non_crossing1 = get_n_non_crossing_from_6_bases(period1)
      else:
        n_non_crossing1 = get_n_non_crossing(period1)
      if len(period2) <= 6:
        n_non_crossing2 = get_n_non_crossing_from_6_bases(period2)
      else:
        n_non_crossing2 = get_n_non_crossing(period2)

      n_non_crossing += n_non_crossing1 * n_non_crossing2

  for G_index in base_indexes['G']:
    for C_index in base_indexes['C']:
      if G_index < C_index:
        left, right = G_index, C_index
      else:
        left, right = C_index, G_index
        
      if (right - left) <= 2 or len(seq) - right <= 2:
        continue
      
      period1 = seq[left+1:right]
      period2 = seq[right+1:] + seq[:left]
      
      if period1.count('A') != period1.count('U') or \
        period1.count('G') != period1.count('C'):
          continue
        
      if len(period1) <= 6:
        n_non_crossing1 = get_n_non_crossing_from_6_bases(period1)
      else:
        n_non_crossing1 = get_n_non_crossing(period1)
      if len(period2) <= 6:
        n_non_crossing2 = get_n_non_crossing_from_6_bases(period2)
      else:
        n_non_crossing2 = get_n_non_crossing(period2)

      n_non_crossing += n_non_crossing1 * n_non_crossing2

  return n_non_crossing


def get_mentioned(clauses, n_vars):
    mentioned = [0] * (n_vars + 1)
    for a, _, _ in clauses:
        mentioned[a[0]] += 1
        mentioned[a[1]] += 1
    return mentioned
  

possible_pairs = get_possible_pairs(rna)
mentioned = get_mentioned(possible_pairs, len(rna))
priority = sorted(range(1, len(rna) + 1), key=lambda x: mentioned[x])


for i, index in enumerate(priority):
  pair = possible_pairs[index][0]
  remained_pairs = possible_pairs[:]
  used_index = [*pair]
  used_paris = [pair]

  while len(remained_pairs) > 0:
    pair2, _, _ = remained_pairs.pop()

    if pair2[0] not in used_index and pair2[1] not in used_index:
      for used_pair in used_paris:
        if used_pair[0] < pair2[0] < used_pair[1] or used_pair[0] < pair2[1] < used_pair[1]:
          break
      else:
        used_index += pair2
        used_paris.append(pair2)

  # print(len(used_index), len(rna))
