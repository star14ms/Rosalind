from util import get_data

data = get_data(__file__)

fasta = data.split('>')
dna1, dna2 = [x.split('\n', 1)[1].replace('\n', '') for x in fasta if x]

n_transitions = 0
n_transversions = 0

for i in range(len(dna1)):
  if dna1[i] != dna2[i]:
    if (dna1[i] in 'AG' and dna2[i] in 'AG') or (dna1[i] in 'CT' and dna2[i] in 'CT'):
      n_transitions += 1
    else:
      n_transversions += 1
      
print(n_transitions / n_transversions)