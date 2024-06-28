### hard
from util import get_data, get_output_path

data = get_data(__file__)
# data = '''>Rosalind_12
# GACTCCTTTGTTTGCCTTAAATAGATACATATTTACTCTTGACTCTTTTGTTGGCCTTAAATAGATACATATTTGTGCGACTCCACGAGTGATTCGTA
# >Rosalind_37
# ATGGACTCCTTTGTTTGCCTTAAATAGATACATATTCAACAAGTGTGCACTTAGCCTTGCCGACTCCTTTGTTTGCCTTAAATAGATACATATTTG'''

fastas = data.split('>')[1:]

for i, fasta in enumerate(fastas):
  with open(get_output_path(f'11_SUBO{i+1}'), 'w') as f:
    f.write('>' + fasta)

# install Lalign
# https://fasta.bioch.virginia.edu/fasta_www2/fasta_down.shtml