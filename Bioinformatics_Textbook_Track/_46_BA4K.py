from util import get_data
from _41_BA4F import score
from constant import INTEGER_MASS_TABLE


def score_linear(peptide, spectrum_theoretical, amino_acid_mass=INTEGER_MASS_TABLE):
    spectrum_expected = LinearSpectrum(peptide, amino_acid_mass)
    return score(spectrum_theoretical, spectrum_expected)


def LinearSpectrum(peptide, amino_acid_mass=INTEGER_MASS_TABLE):
    prefix_mass = [0]
    for i in range(len(peptide)):
        for j in range(20):
            if list(amino_acid_mass.keys())[j] == peptide[i]:
                prefix_mass.append(prefix_mass[-1] + list(INTEGER_MASS_TABLE.values())[j])

    linear_spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])

    return sorted(linear_spectrum)


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''NQEL
# 0 99 113 114 128 227 257 299 355 356 370 371 484'''

    peptides, spectrum = data.split('\n')
    spectrum_theoretical = list(map(int, spectrum.split()))

    number = score_linear(peptides, spectrum_theoretical)
    print(number)
