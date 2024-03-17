from util import get_data

dna = get_data(__file__)
# dna = '''>Rosalind_6431
# CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
# CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
# TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
# AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
# GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
# CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
# CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG'''
dna = dna.split('\n', 1)[1].replace('\n', '')

# 4-mer composition list
kmer_list = ['A', 'C', 'G', 'T']
kmer_dict = {}
for i in kmer_list:
    for j in kmer_list:
        for k in kmer_list:
            for l in kmer_list:
                kmer = i + j + k + l
                kmer_dict[kmer] = 0
                
print(kmer_dict)

# Count 4-mer composition
for i in range(len(dna) - 3):
    kmer = dna[i:i+4]
    kmer_dict[kmer] += 1

print(' '.join(map(str, list(kmer_dict.values()))))
