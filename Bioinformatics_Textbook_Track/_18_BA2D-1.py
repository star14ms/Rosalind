### hard
from util import get_data
from _2_BA1B import most_famous_k_mer
from _17_BA2C import get_profile_most_probable_kmer


def create_profile(motifs):
    profile = {nucleotide: [1/(len(motifs) * 2)]*len(motifs[0]) for nucleotide in "ACGT"}
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        for nucleotide in "ACGT":
            profile[nucleotide][i] = (column.count(nucleotide) + 1) / (len(motifs) + 4)  # pseudocounts
    return profile


def greedy_motif_search(texts, k, t):
    best_moitifs = [most_famous_k_mer(text, k) for text in texts]
    
    for i in range(len(texts[0]) - k + 1):
        motifs = [motifs_first_string := texts[0][i:i+k]]
        print(motifs_first_string)

        for j in range(1, t):
            profile = create_profile(motifs_first_string)
            print(profile)
            next_motif = get_profile_most_probable_kmer(texts[j], k, profile)
            motifs.append(next_motif)

        # if score(motifs) < score(best_moitifs):
        #     best_moitifs = motifs
            
    return best_moitifs


if __name__ == "__main__":
    # data = get_data(__file__)
    data ='''3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG'''

    data = data.split('\n')
    k, t = map(int, data[0].split())
    dnas = data[1:]

    k_mer = greedy_motif_search(dnas, k, t)
    print(k_mer)
