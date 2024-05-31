from util import get_data, get_output_path
from _1_BA1A import pattern_count
from _2_BA1B import get_k_mers


def get_Lt_clumps(k_mers):
    k_mers_t_times = list(filter(lambda key: k_mers[key] >= t, k_mers.keys()))

    k_mers_forming_Lt_clumps = []
    for k_mer in k_mers_t_times:
        for i in range(len(genome) - L + 1):
            period = genome[i:i+L]
            if pattern_count(period, k_mer) == t:
                k_mers_forming_Lt_clumps.append(k_mer)
                break
            
    return k_mers_forming_Lt_clumps


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
# 5 75 4'''

    genome, integers = data.split("\n")
    k, L, t = map(int, integers.split())
    
    k_mers = get_k_mers(genome, k)
    k_mers_forming_Lt_clumps = get_Lt_clumps(k_mers)

    with open(get_output_path(__file__), "w") as f:
        print(*k_mers_forming_Lt_clumps, sep=' ')
        print(*k_mers_forming_Lt_clumps, sep=' ', file=f)
