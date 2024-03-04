from util import get_data
from constant import CODON_TABLE
from collections import Counter

seq = get_data(__file__)

counter = Counter(CODON_TABLE.values())
total = 1
for amino_acid in list(seq) + ['-']:
    total *= counter[amino_acid]

print(total % 1000000)    
