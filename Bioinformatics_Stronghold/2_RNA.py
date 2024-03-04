
with open('data/rosalind_rna.txt', 'r') as f:
    dna = f.read().strip()
    rna = dna.replace('T', 'U')
    print(rna)