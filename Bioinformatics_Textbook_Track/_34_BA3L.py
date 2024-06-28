from util import get_data, get_output_path
from _32_BA3J import read_paired_kmers, reconstruct_string_from_paired_kmers


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''4 2
# GACC|GCGC
# ACCG|CGCC
# CCGA|GCCG
# CGAG|CCGG
# GAGC|CGGA'''

    integers, paired_kmers_str = data.split('\n', 1)
    k, d = tuple(map(int, integers.split()))
    paired_kmers_str = paired_kmers_str.split('\n')
    
    paired_kmers = read_paired_kmers(paired_kmers_str)
    text = reconstruct_string_from_paired_kmers(paired_kmers, d)

    with open(get_output_path(__file__), "w") as f:
        print(text)
        print(text, file=f)
