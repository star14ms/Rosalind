from util import get_data
from _41_BA4F import score_cyclic
from constant import INTEGER_MASS_TABLE


def expand(leader_board, masses=None):
    masses = masses or set(INTEGER_MASS_TABLE.values())
    return [leader + [mass] for leader in leader_board for mass in masses]


def LeaderboardCyclopeptideSequencing(spectrum, N, masses=None, verbose=False):
    leader_board = [[]]
    leader_peptide = []
    while leader_board:
        leader_board = expand(leader_board, masses=masses)
        
        for i in range(len(leader_board)-1, -1, -1):
            if sum(leader_board[i]) == spectrum[-1] and \
                score_cyclic(leader_board[i], spectrum) > score_cyclic(leader_peptide, spectrum):
                leader_peptide = leader_board[i]
            elif sum(leader_board[i]) > spectrum[-1]:
                del leader_board[i]
        
        scores = {str(leader): score_cyclic(leader, spectrum) for leader in leader_board}
        if verbose:
            print(sorted(list(scores.values()), reverse=True)[:20])
        leader_board = sorted(leader_board, key=lambda masses: scores[str(masses)], reverse=True)[:N]
        
    return leader_peptide


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''10
# 0 71 113 129 147 200 218 260 313 331 347 389 460'''

    N, spectrum = data.splitlines()
    spectrum = list(map(int, spectrum.split()))

    leader_peptide = LeaderboardCyclopeptideSequencing(spectrum, int(N))

    print("-".join(map(str, leader_peptide)))
