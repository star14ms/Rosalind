### medium
from util import get_data
from _7_BA1G import hamming_distance
from itertools import product


def get_k_mers(seq, k, d_mismatches_at_most=0):
    possible_k_mer_substrings = [seq[i:i+k] for i in range(len(seq) - k + 1)]

    k_mers_with_frequency = {}
    for k_mer1 in product("ACGT", repeat=k):
        k_mer1 = ''.join(k_mer1); # Convert tuple to string
        for k_mer2 in possible_k_mer_substrings:
            if hamming_distance(k_mer1, k_mer2) <= d_mismatches_at_most:
                k_mers_with_frequency[k_mer1] = k_mers_with_frequency.get(k_mer1, 0) + 1

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
