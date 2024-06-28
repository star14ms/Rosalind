from util import get_data
from Bio.Seq import translate

data = get_data(__file__)
# data = '''ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
# MAMAPRTEINSTRING'''

dna, protein = data.split('\n')
translated_protein = translate(dna)

for i in range(len(protein)):
  if translated_protein[i] == protein[i]:
    print(i+1)
    break
