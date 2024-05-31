### ChatGPT: https://chatgpt.com/share/bf0d2a1f-5135-4356-a300-7a95393d6af6
from util import get_data, get_output_path


def profile_most_probable_kmer(dna, k, profile):
    n = len(dna)
    max_prob = -1
    best_kmer = dna[0:k]
    for i in range(n-k+1):
        kmer = dna[i:i+k]
        prob = 1
        for j, nucleotide in enumerate(kmer):
            prob *= profile[nucleotide][j]
        if prob > max_prob:
            max_prob = prob
            best_kmer = kmer
    return best_kmer

def create_profile(motifs):
    profile = {nucleotide: [1/(len(motifs) * 2)]*len(motifs[0]) for nucleotide in "ACGT"}
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        for nucleotide in "ACGT":
            profile[nucleotide][i] = (column.count(nucleotide) + 1) / (len(motifs) + 4)  # pseudocounts
    return profile

def score(motifs):
    consensus = ''
    k = len(motifs[0])
    for j in range(k):
        freq = {nucleotide: 0 for nucleotide in "ACGT"}
        for i in range(len(motifs)):
            freq[motifs[i][j]] += 1
        consensus += max(freq, key=freq.get)
    score = 0
    for motif in motifs:
        for i in range(len(motif)):
            if motif[i] != consensus[i]:
                score += 1
    return score

def greedy_motif_search(dna, k, t):
    best_motifs = [seq[:k] for seq in dna]
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i+k]]
        for j in range(1, t):
            profile = create_profile(motifs)
            next_motif = profile_most_probable_kmer(dna[j], k, profile)
            motifs.append(next_motif)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''3 5
# GGCGTTCAGGCA
# AAGAATCAGTCA
# CAAGGAGTTCGC
# CACGTCAATCAC
# CAATAATATTCG'''

    data = data.split('\n')
    k, t = map(int, data[0].split())
    dnas = data[1:]

    k_mer = greedy_motif_search(dnas, k, t)
    
    with open(get_output_path(__file__), 'w') as f:
        print(*k_mer, sep='\n')
        print(*k_mer, sep='\n', file=f)
