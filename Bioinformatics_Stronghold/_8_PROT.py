from util import get_data
from constant import CODON_TABLE

data = get_data(__file__)

protein = ''

for i in range(0, len(data), 3):
    codon = data[i:i+3]
    if CODON_TABLE[codon] == '-':
        break
    protein += CODON_TABLE[codon]

print(protein)