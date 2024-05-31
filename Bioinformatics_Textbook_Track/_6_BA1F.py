from util import get_data


def get_values_of_skew(seq):
    skew = [0]
    for i in range(1, len(seq) + 1):
        if seq[i-1] == 'C':
            skew.append(skew[i-1] - 1)
        elif seq[i-1] == 'G':
            skew.append(skew[i-1] + 1)
        else:
            skew.append(skew[i-1])
    return skew


if __name__ == "__main__":
    genome = get_data(__file__)
    # genome = '''CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG'''

    skew = get_values_of_skew(genome)

    min_skew = min(skew)
    idxs_of_min_skew = [i for i, s in enumerate(skew) if s == min(skew)]
    
    print(*idxs_of_min_skew, sep=' ')
