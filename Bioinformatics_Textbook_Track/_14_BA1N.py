from util import get_data, get_output_path
from _7_BA1G import hamming_distance
from itertools import product


def get_neighbors(pattern, d):
    neighbors = []
    for pattern2 in product("ACGT", repeat=len(pattern)):
        pattern2 = ''.join(pattern2)
        if hamming_distance(pattern, pattern2) <= d:
            neighbors.append(pattern2)
    return neighbors


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''ACG
# 1'''

    pattern, d = data.split()

    neighbors = get_neighbors(pattern, int(d))
    
    with open(get_output_path(__file__), "w") as f:
        print(*neighbors, sep="\n")
        print(*neighbors, sep="\n", file=f)
