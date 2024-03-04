from util import get_data, rna_to_protein_strings, find_orf

data = get_data(__file__)

dna = ''.join(data.split('\n')[1:])
rna = dna.replace('T', 'U')

seqs = rna_to_protein_strings(rna)
orf = find_orf(seqs, r'M.*?-')
print(*orf, sep='\n')
