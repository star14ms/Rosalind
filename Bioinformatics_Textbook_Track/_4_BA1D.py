from util import get_data, get_output_path, reverse_complement


def find_where_patterns_appear_in_genome(genome, pattern):
    pattern_len = len(pattern)
    genome_len = len(genome)
    positions = []
    for i in range(genome_len - pattern_len + 1):
        if genome[i:i+pattern_len] == pattern:
            positions.append(i)
    return positions


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''ATAT
# GATATATGCATATACTT'''

    pattern, genome = data.split("\n")
    positions = find_where_patterns_appear_in_genome(genome, pattern)
    
    with open(get_output_path(__file__), "w") as f:
        print(*positions, sep=' ')
        print(*positions, sep=' ', file=f)
