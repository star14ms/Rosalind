from util import get_data

dna = get_data(__file__)

print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))
