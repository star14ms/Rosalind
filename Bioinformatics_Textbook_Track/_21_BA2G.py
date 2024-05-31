from util import get_data, get_output_path
from _19_BA2E import create_profile, score
from _20_BA2F import get_random_motifs
import random
from tqdm import tqdm


# Pr(Pattern | Profile)
def profile_randomly_generated_kmer(seq, k, profile):
    n = len(seq)
    probs = []
    for i in range(n - k + 1):
        kmer = seq[i:i+k]
        prob = 1
        for j, base in enumerate(kmer):
            prob *= profile[base][j]
        probs.append(prob)
    
    total_prob = sum(probs)
    probs = [prob / total_prob for prob in probs]
    i = random.choices(list(range(n - k + 1)), weights=probs)[0]
    return seq[i:i+k]


def GibbsSampler(Dna, k, t, N):
    motifs = get_random_motifs(Dna, k)
    best_motifs = motifs

    for _ in range(N):
        i = random.randint(0, t-1)
        profile = create_profile(motifs[:i] + motifs[i+1:])
        motifs[i] = profile_randomly_generated_kmer(Dna[i], k, profile)

        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs, score(best_motifs)


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''8 5 100
# CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
# GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
# TAGTACCGAGACCGAAAGAAGTATACAGGCGT
# TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
# AATCCACCAGCTCCACGTGCAATGTTGGCCTA'''

    data = data.split('\n')
    k, t, N = map(int, data[0].split())
    dnas = data[1:]

    best_motifs = None
    best_score = None
    for i in tqdm(range(64)):
        best_motif_current, best_score_current = GibbsSampler(dnas, k, t, N)

        if best_score is None or best_score_current < best_score:
            best_motifs = best_motif_current
            best_score = best_score_current
            print(best_score)
    
    with open(get_output_path(__file__), 'w') as f:
        print(*best_motifs, sep='\n')
        print(*best_motifs, sep='\n', file=f)
    print(best_score)
