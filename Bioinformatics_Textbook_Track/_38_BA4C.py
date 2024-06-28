from util import get_data, get_output_path
from constant import INTEGER_MASS_TABLE


def Cyclospectrum(peptides):
    masses_of_subpeptides = [0]
    for len_subpeptide in range(1, len(peptides)):
        for i in range(len(peptides)):
            subpeptide = (peptides + peptides)[i:i+len_subpeptide]
            masses_of_subpeptides.append(sum(INTEGER_MASS_TABLE[peptide] for peptide in subpeptide))
    
    masses_of_subpeptides.append(sum(INTEGER_MASS_TABLE[peptide] for peptide in peptides))
    return sorted(masses_of_subpeptides)


if __name__ == "__main__":
    peptides = get_data(__file__)
    # peptides ='''LEQN'''

    spectrum = Cyclospectrum(peptides)

    with open(get_output_path(__file__), "w") as f:
        print(*spectrum)
        print(*spectrum, file=f)
        