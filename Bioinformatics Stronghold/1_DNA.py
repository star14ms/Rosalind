
with open('data/rosalind_dna.txt', 'r') as f:
    dna = f.read().strip()
    print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))