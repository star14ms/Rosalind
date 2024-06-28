from util import get_data
from collections import Counter

data = get_data(__file__)


def consensus_and_profile(data):
    data = data.split('>')
    dna_list = [''.join(dna.split('\n')[1:]) for dna in data if dna]
    profile = { 'A': [], 'C': [], 'G': [], 'T': []}
    consensus = ''

    for i in range(len(dna_list[0])):
        index_i_bases = ''.join([dna[i] for dna in dna_list])
        counter = Counter(index_i_bases)
        consensus += counter.most_common(1)[0][0]

        for base in 'ACGT':
            profile[base].append(counter.get(base, 0))

    return consensus, profile


consensus, profile = consensus_and_profile(data)


print(consensus)
print('A:', ' '.join(map(str, profile['A'])))
print('C:', ' '.join(map(str, profile['C'])))
print('G:', ' '.join(map(str, profile['G'])))
print('T:', ' '.join(map(str, profile['T'])))