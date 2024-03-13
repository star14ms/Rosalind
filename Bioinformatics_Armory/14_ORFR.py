from util import get_data
from Bio.Seq import translate, reverse_complement

dna = get_data(__file__)
# data = '''AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
# '''

# copilot: make a function input: one reading frame, output: every possible orfs from input
def get_orfs(protein):
  orfs = []
  for i in range(len(protein)):
    if protein[i] == 'M':
      if '*' in protein[i:]:
        orf = protein[i:][:protein[i:].index('*')]
        orfs.append(orf)
  return orfs

longest_orf = []

for dna in [dna, reverse_complement(dna)]:
  for i in range(3):
    trim = -(len(dna[i:]) % 3)
    protein_string = translate(dna[i:trim])
    orfs = get_orfs(protein_string)
    
    if orfs != []:
      longest_orf = max(orfs + [longest_orf], key=len)

print(longest_orf)
