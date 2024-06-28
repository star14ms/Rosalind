from util import get_data, get_output_path


def kmer_composition(text, k):
    kmers = []
    for i in range(len(text) - k + 1):
        kmers.append(text[i:i+k])
    return sorted(kmers)


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''5
# CAATCCAAC'''

    k, text = data.split('\n')
    distance = kmer_composition(text, int(k))

    with open(get_output_path(__file__), "w") as f:
        print(*distance, sep='\n')
        print(*distance, sep='\n', file=f)
