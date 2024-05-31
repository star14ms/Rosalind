from util import get_data


def get_k_mers(seq, k):
    k_mers = {}
    for i in range(len(seq) - k + 1):
        k_mer = seq[i:i+k]
        k_mers[k_mer] = k_mers.get(k_mer, 0) + 1
        
    return k_mers


def most_famous_k_mer(seq, k):
    k_mers = get_k_mers(seq, k)
    max_count = max(k_mers.values())
    return [k_mer for k_mer, count in k_mers.items() if count == max_count]


if __name__ == "__main__":
    data = get_data(__file__)
    # data ='''ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4'''

    seq, k = data.splitlines()

    # Calculate and print the result
    count = most_famous_k_mer(seq, int(k))
    print(*count, sep=" ")
