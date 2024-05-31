### medium
from util import get_data, get_output_path
from _19_BA2E import profile_most_probable_kmer, create_profile, score
import random
from tqdm import tqdm


def get_random_motifs(Dna, k):
    motifs = []
    for seq in Dna:
        i = random.randint(0, len(seq) - k)
        motifs.append(seq[i:i+k])
    return motifs


def RandomizedMotifSearch(Dna, k, n_iter=1000):
    best_motifs_overall = None
    best_score_overall = None

    for _ in tqdm(range(n_iter)):
        motifs = get_random_motifs(Dna, k)
        best_motifs = motifs
        score_best_motifs = score(best_motifs)

        while True:
            profile = create_profile(motifs)
            motifs = [profile_most_probable_kmer(seq, k, profile) for seq in Dna]

            score_motifs = score(motifs)
            if score_motifs < score_best_motifs:
                best_motifs = motifs
                score_best_motifs = score_motifs
            else:
                break

        if best_score_overall is None or score_best_motifs < best_score_overall:
            best_motifs_overall = best_motifs
            best_score_overall = score_best_motifs
            print(best_score_overall)

    return best_motifs_overall, best_score_overall


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''8 5
# CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
# GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
# TAGTACCGAGACCGAAAGAAGTATACAGGCGT
# TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
# AATCCACCAGCTCCACGTGCAATGTTGGCCTA'''

    data = data.split('\n')
    k, t = map(int, data[0].split())
    dnas = data[1:]

    best_motifs, best_score = RandomizedMotifSearch(dnas, k, n_iter=1000)
    
    with open(get_output_path(__file__), 'w') as f:
        print(*best_motifs, sep='\n')
        print(*best_motifs, sep='\n', file=f)
    
    print(best_score)
