from util import get_data, get_output_path
from _7_BA1G import hamming_distance


def positions_of_substring_of_text(pattern, text, d_mismatches_at_most):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i+len(pattern)], pattern) <= d_mismatches_at_most:
            positions.append(i)
            
    return positions


if __name__ == "__main__":
    data = get_data(__file__)
#     data = '''ATTCTGGA
# CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
# 3'''

    pattern, text, d_mismatches = data.split('\n')
    positions = positions_of_substring_of_text(pattern, text, int(d_mismatches))

    with open(get_output_path(__file__), "w") as f:
        print(*positions)
        print(*positions, file=f)
