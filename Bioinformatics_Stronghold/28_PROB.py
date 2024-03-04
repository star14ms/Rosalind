from util import get_data
import numpy as np
from numpy import log10

data = get_data(__file__)

dna, posibilities = data.split('\n')
posibilities = np.array(list(map(float, posibilities.split(' '))))

gc_content = posibilities
g_or_c = gc_content / 2
at_content = 1 - gc_content
a_or_t = at_content / 2

possibility = np.ones(len(posibilities))
for base in dna:
  if base in 'GC':
    possibility *= g_or_c
  else:
    possibility *= a_or_t

print(*log10(possibility))

