from util import get_data, get_output_path
from _7_BA1G import hamming_distance
from itertools import product


def motif_enumeration(dnas, k, d):
    kd_motifs = set()
    for pattern in product("ACGT", repeat=k):
        if all(
          any(hamming_distance(dna[i:i+k], ''.join(pattern)) <= d \
              for i in range(len(dna) - k + 1)
        ) for dna in dnas):
          kd_motifs.add(''.join(pattern))

    return kd_motifs


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''3 1
# ATTTGGC
# TGCCTTA
# CGGTATC
# GAAAATT'''

    data = data.split('\n')
    k, d = map(int, data[0].split())
    dnas = data[1:]

    kd_motifs = motif_enumeration(dnas, int(k), int(d))

    with open(get_output_path(__file__), "w") as f:
        print(*kd_motifs, sep="\n")
        print(*kd_motifs, sep="\n", file=f)
