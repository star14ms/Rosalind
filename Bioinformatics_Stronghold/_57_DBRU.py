from util import get_data, get_output_path
from Bio.Seq import Seq

data = get_data(__file__)
# data = '''TGAT
# CATG
# TCAT
# ATGC
# CATC
# CATC'''

dnas = data.split('\n')

n_mer = len(dnas[0])-1
adjacency_list = set()

for dna in dnas:
  my_seq = Seq(dna)
  reverse_complement = str(my_seq.reverse_complement())
  
  for i in range(len(dna)-n_mer):
    key = (dna[i:i+n_mer], dna[i+1:i+n_mer+1])
    adjacency_list.add(key)
    
    key = (reverse_complement[i:i+n_mer], reverse_complement[i+1:i+n_mer+1])
    adjacency_list.add(key)


adjacency_list = sorted(adjacency_list)


with open(get_output_path(__file__), 'w') as f:
  for adjacency in adjacency_list:
    print('(' + ', '.join(adjacency) + ')')
    f.write('(' + ', '.join(adjacency) + ')\n')


print(len(adjacency_list), len(dnas[0]))
