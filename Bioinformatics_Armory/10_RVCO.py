from util import get_data, get_output_path
from Bio.Seq import Seq

data = get_data(__file__)
# data ='''>Rosalind_64
# ATAT
# >Rosalind_48
# GCATA'''
data = data.split('>')[1:]
dnas = list(map(lambda a: a.split('\n', 1)[-1].replace('\n', ''), data))

n_count = 0
for dna in dnas:
  my_seq = Seq(dna)
  reversed_seq = my_seq.reverse_complement()
  
  if my_seq == reversed_seq:
    n_count += 1
    
print(n_count)
