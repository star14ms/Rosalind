from util import get_data, reverse_complement
from _7_BA1G import hamming_distance
from itertools import product


def get_k_mers(seq, k, d_mismatches_at_most=0):
    seq_fractions = [seq[i:i+k] for i in range(len(seq) - k + 1)]

    k_mers_with_frequency = {}
    for pattern in product("ACGT", repeat=k):
        pattern = ''.join(pattern); # Convert tuple to string
        for seq_frac in seq_fractions:
            if hamming_distance(pattern, seq_frac) <= d_mismatches_at_most:
                k_mers_with_frequency[pattern] = k_mers_with_frequency.get(pattern, 0) + 1
            if hamming_distance(reverse_complement(pattern), seq_frac) <= d_mismatches_at_most:
                k_mers_with_frequency[pattern] = k_mers_with_frequency.get(pattern, 0) + 1

    return k_mers_with_frequency


def most_famous_k_mer(seq, k, d_mismatches_at_most=0):
    k_mers = get_k_mers(seq, k, d_mismatches_at_most)
    max_count = max(k_mers.values())
    return [k_mer for k_mer, count in k_mers.items() if count == max_count]


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4 1'''

    seq, integers = data.splitlines()
    k, d = integers.split()

    count = most_famous_k_mer(seq, int(k), int(d))

    print(*count, sep=" ")
