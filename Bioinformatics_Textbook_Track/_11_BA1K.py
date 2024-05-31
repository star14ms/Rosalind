from util import get_data, get_output_path
from itertools import product


def get_frequency_array(seq, k):
    frequency_array = {}
    for pattern in product("ACGT", repeat=k):
        pattern = ''.join(pattern)

        if pattern not in frequency_array:
            frequency_array[pattern] = 0

        for i in range(len(seq) - k + 1):
            if seq[i:i + k] == pattern:
                    frequency_array[pattern] += 1

    return frequency_array


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''ACGCGGCTCTGAAA
# 2'''

    dna, k = data.splitlines()
    
    frequency_array = get_frequency_array(dna, int(k))
    
    with open(get_output_path(__file__), "w") as f:
        print(*frequency_array.values(), sep=" ")
        print(*frequency_array.values(), sep=" ", file=f)
