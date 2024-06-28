from util import get_data
from _38_BA4C import Cyclospectrum
from _40_BA4E import Cyclospectrum_from_masses


def score(theoretical, expected):
    score = 0
    theoretical = theoretical.copy()
    for mass in expected:
        if mass in theoretical:
            score += 1
            theoretical.remove(mass)

    return score


def score_cyclic(peptide, expected):
    if len(peptide) > 0 and isinstance(peptide[0], str):
        theoretical = Cyclospectrum(peptide)
    else: 
        theoretical = Cyclospectrum_from_masses(peptide)
        
    return score(theoretical, expected)
    

if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''NQEL
# 0 99 113 114 128 227 257 299 355 356 370 371 484'''

    peptides, spectrum = data.splitlines()
    spectrum = list(map(int, spectrum.split()))

    spectrum_from_peptides = Cyclospectrum(peptides)
    score = score_cyclic(peptides, spectrum)
    
    print(score)
