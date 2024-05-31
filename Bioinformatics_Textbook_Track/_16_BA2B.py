from util import get_data
from _7_BA1G import hamming_distance
from itertools import product


def get_median_strings(dnas, k):
    min_hamm_distances = {}
    for pattern in product("ACGT", repeat=k):
        pattern = ''.join(pattern)
        
        min_hamm_distance = 0
        for dna in dnas:
            min_hamm_distance += min(hamming_distance(pattern, dna[i:i+k]) for i in range(len(dna) - k + 1))
        min_hamm_distances[pattern] = min_hamm_distance
        
    midean_str = min(min_hamm_distances, key=min_hamm_distances.get)
    return list(filter(lambda key: min_hamm_distances[key] == min_hamm_distances[midean_str], min_hamm_distances))


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''3
# AAATTGACGCAT
# GACGACCACGTT
# CGTCAGCGCCTG
# GCTGAGCACCGG
# AGTACGGGACAG'''

    data = data.split('\n')
    k = int(data[0])
    dnas = data[1:]

    median_strings = get_median_strings(dnas, int(k))

    print(*median_strings)
