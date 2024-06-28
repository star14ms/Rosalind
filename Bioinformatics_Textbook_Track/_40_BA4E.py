from util import get_data, get_output_path
from constant import INTEGER_MASS_TABLE
import math
from itertools import permutations
from tqdm import tqdm


def Cyclospectrum_from_masses(masses):
    masses_of_subpeptides = [0]
    for len_subpeptide in range(1, len(masses)):
        for i in range(len(masses)):
            subpeptide = (masses + masses)[i:i+len_subpeptide]
            masses_of_subpeptides.append(sum(subpeptide))
    
    masses_of_subpeptides.append(sum(masses))
    return sorted(masses_of_subpeptides)


def ideal_spectrum_to_peptides(spectrum):
    len_seq = math.ceil((len(spectrum) - 2) ** (1/2))

    masses_amino_acid = []
    for mass in spectrum:
        if mass in INTEGER_MASS_TABLE.values():
            masses_amino_acid.append(mass)
            if len(masses_amino_acid) == len_seq:
                break
    
    peptides_matched_to_spectrum = []
    for peptides in tqdm(permutations(masses_amino_acid, len_seq), total=math.perm(len(masses_amino_acid))):
        for i in range(len(peptides)-1):
            if sum(peptides[i:i+2]) not in spectrum:
                break
        else:
            if spectrum == Cyclospectrum_from_masses(peptides):
                peptides_matched_to_spectrum.append(peptides)

    # peptides_matched_to_spectrum = []
    # for i in range(len(masses_amino_acid)):
    #     peptides_matched_to_spectrum.append((masses_amino_acid + masses_amino_acid)[i: i + len_seq])
    #     peptides_matched_to_spectrum.append((masses_amino_acid + masses_amino_acid)[len_seq+i: i: -1])

    return set(peptides_matched_to_spectrum)


if __name__ == "__main__":
    data = get_data(__file__)
    # data ='''0 113 128 186 241 299 314 427'''
    
    spectrum = list(map(int, data.split()))
    peptides = ideal_spectrum_to_peptides(spectrum)

    with open(get_output_path(__file__), "w") as f:
        for peptide in peptides:
            print(*peptide, sep='-', end=' ')
            print(*peptide, sep='-', end=' ', file=f)
    print()
    