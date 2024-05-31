from util import get_data
from _7_BA1G import hamming_distance


def DistanceBetweenPatternAndStrings(pattern, dnas):
    k = len(pattern)
    distance = 0
    for dna in dnas:
        hamming_distance_min = float('inf')
        
        for i in range(len(dna) - k + 1):
            kmer = dna[i:i+k]
            hamming_distance_min = min(hamming_distance_min, hamming_distance(pattern, kmer))
        distance += hamming_distance_min

    return distance


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''AAA
# TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT'''

    pattern, dnas = data.split('\n')
    dnas = dnas.split()
    distance = DistanceBetweenPatternAndStrings(pattern, dnas)

    print(distance)
