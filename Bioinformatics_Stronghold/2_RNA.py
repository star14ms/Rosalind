from util import get_data

dna = get_data(__file__)

rna = dna.replace('T', 'U')
print(rna)