from util import get_data, get_output_path
import numpy as np

data = get_data(__file__)
# data = '''GACCACGGTT
# ACAG
# GT
# CCG'''

dnas = data.split('\n')
source_dna = dnas.pop(0)

# check if the two dna stirngs can be interwoven into the source dna string
def is_interwoven(source, dna1, dna2):
    if len(dna1) + len(dna2) != len(source):
        return False
    i = 0
    j = 0
    for c in source:
        if i < len(dna1) and c == dna1[i]:
            i += 1
        elif j < len(dna2) and c == dna2[j]:
            j += 1
        else:
            return False
    return True

# check if a part of the source string can be interwoven with the given DNA strings
def is_partial_interwoven(source, dna1, dna2, start, end):
  if end - start != len(dna1) + len(dna2):
    return False
  i = 0
  j = 0
  for c in source[start:end]:
    if i < len(dna1) and c == dna1[i]:
      i += 1
    elif j < len(dna2) and c == dna2[j]:
      j += 1
    else:
      return False
  return True


# calculate the interwoven matrix
matrix = np.zeros((len(dnas), len(dnas)), dtype=int)
for idx1 in range(len(dnas)):
  for idx2 in range(idx1, len(dnas)):
    for start in range(len(source_dna) - len(dnas[idx1]) - len(dnas[idx2]) + 1):
      end = start + len(dnas[idx1]) + len(dnas[idx2])
      if is_partial_interwoven(source_dna, dnas[idx1], dnas[idx2], start, end):
        matrix[idx1][idx2] = 1
        matrix[idx2][idx1] = 1

print(matrix)

with open(get_output_path(__file__), 'w') as f:
  for row in matrix:
    f.write(' '.join(map(str, row)) + '\n')