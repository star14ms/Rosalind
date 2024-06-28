from util import get_data
from _46_BA4K import score_linear
from constant import INTEGER_MASS_TABLE


def trim_leaderboard(leaderboard, spectrum, N, amino_acid_mass=INTEGER_MASS_TABLE):
    linear_scores = {}
    for peptide in leaderboard:
        linear_scores[peptide] = score_linear(peptide, spectrum, amino_acid_mass)
    
    sorted_peptides = sorted(leaderboard, key=lambda x: linear_scores[x], reverse=True)
    if len(sorted_peptides) <= N:
        return sorted_peptides
    
    Nth_score = linear_scores[sorted_peptides[N-1]]
    for i in range(N, len(sorted_peptides)):
        if linear_scores[sorted_peptides[i]] < Nth_score:
            return sorted_peptides[:i]
    
    return sorted_peptides


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''LAST ALST TLLT TQAS
# 0 71 87 101 113 158 184 188 259 271 372
# 2'''

    leaderboard, spectrum, N = data.split('\n')
    leaderboard = leaderboard.split()
    spectrum = list(map(int, spectrum.split()))

    top_N_peptides = trim_leaderboard(leaderboard, spectrum, int(N))

    print(' '.join(top_N_peptides))
