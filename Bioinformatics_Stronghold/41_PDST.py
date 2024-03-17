from util import get_data, get_output_path
import numpy as np

# how to force to print 5 decimal places
np.set_printoptions(formatter={'all':lambda x: '%.5f' % x})

data = get_data(__file__)
# data ='''>Rosalind_9499
# TTTCCATTTA
# >Rosalind_0942
# GATTCATTTC
# >Rosalind_6568
# TTTCCATTTT
# >Rosalind_1833
# GTTCCATTTA'''

dnas = data.split('>')[1:]
dnas = [dna.split('\n', 1)[1].replace('\n', '') for dna in dnas]

# p-distance between sequences
# Given: DNA strings s and t of equal length (not exceeding 1 kbp).

embedding = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
p_distances = np.zeros([len(dnas), len(dnas)], dtype=float)

for i in range(len(dnas)):
    for j in range(len(dnas)):
        if i != j:
          x = np.array([embedding[base] for base in dnas[i]])
          y = np.array([embedding[base] for base in dnas[j]])
          p_distance = np.sum(np.where(x != y, 1 / len(dnas[0]), 0))
          p_distances[i, j] = p_distance
          
p_distances = p_distances.tolist()

with open(get_output_path(__file__), 'w') as output_data:
    for row in p_distances:
        output_data.write(' '.join(map(lambda x: '%5f' % x, row)) + '\n')
        print(' '.join(map(lambda x: '%5f' % x, row)))
