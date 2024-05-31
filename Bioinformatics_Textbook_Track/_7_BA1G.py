from util import get_data


def hamming_distance(seq1, seq2):
    """Calculate the Hamming distance between two sequences."""
    return sum(ch1 != ch2 for ch1, ch2 in zip(seq1, seq2))


if __name__ == "__main__":
    data = get_data(__file__)
#     data = '''GGGCCGTTGGT
# GGACCGTTGAC'''

    dna1, dna2 = data.split('\n')
    hamm_distance = hamming_distance(dna1, dna2)
    
    print(hamm_distance)
