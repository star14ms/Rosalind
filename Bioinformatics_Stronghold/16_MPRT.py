# error
from util import get_data
from urllib.request import urlopen as get

data = get_data(__file__)

fasta_ids = data.split('\n')

# N-glycosylation motif: N{P}[ST]{P}
# N: asparagine, P: any amino acid except aspartic acid, S: serine, T: threonine

location_motif = {}

for id in fasta_ids:
  # fasta = get(f'https://rest.uniprot.org/unisave/{id.split('_')[0]}?format=fasta&versions={id}')
  fasta = get(f'http://www.uniprot.org/uniprot/{id.split('_')[0]}.fasta').read().decode('utf-8')
  seq = ''.join(fasta.split('\n')[1:])

  # n-glycosylation motif test
  for i in range(len(seq) - 4):
    if seq[i] == 'N' and seq[i + 1] != 'P' and seq[i + 2] in ['S', 'T'] and seq[i + 3] != 'P':
      if location_motif.get(id) == None:
        location_motif[id] = [i + 1]
        print(id)
      else:
        location_motif[id].append(i + 1)

  if location_motif.get(id) != None:
    print(*location_motif.get(id))


with open('output/16_MPRT.txt', 'w') as f:
  for key, value in location_motif.items():
    f.write(key + '\n')
    f.write(' '.join(map(str, value)) + '\n')
