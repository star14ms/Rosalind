from util import get_data, rna_to_protein_strings

data = get_data(__file__)

fastas = data.split('>')[1:]
dnas = [dna.split('\n', 1)[1].replace('\n', '') for dna in fastas]

dna = dnas[0]
for substring in dnas[1:]:
    dna = dna.replace(substring, '')

rna = dna.replace('T', 'U')
seqs = rna_to_protein_strings(rna)

print(seqs[0])
# print(*seqs, sep='\n')

