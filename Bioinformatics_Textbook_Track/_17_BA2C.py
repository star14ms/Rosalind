from util import get_data


def get_profile_most_probable_kmer(text, k, matrix_profile):
    prob_k_mers = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        
        prob = 1
        for i, base in enumerate(pattern):
            prob *= matrix_profile['ACGT'.index(base)][i]
        prob_k_mers[pattern] = prob

    return max(prob_k_mers, key=prob_k_mers.get)


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
# 5
# 0.2 0.2 0.3 0.2 0.3
# 0.4 0.3 0.1 0.5 0.1
# 0.3 0.3 0.5 0.2 0.4
# 0.1 0.2 0.1 0.1 0.2'''

    data = data.split('\n', 2)
    text = data[0]
    k = int(data[1])
    matrix_profile = list(map(lambda x: list(map(float, x.split())), data[2].split('\n')))

    k_mer = get_profile_most_probable_kmer(text, k, matrix_profile)

    print(k_mer)
