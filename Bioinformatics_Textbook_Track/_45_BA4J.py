from util import get_data, get_output_path
from constant import INTEGER_MASS_TABLE


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
    peptides = get_data(__file__)
    # peptides ='''NQEL'''

    spectrum = LinearSpectrum(peptides)

    with open(get_output_path(__file__), "w") as f:
        print(*spectrum)
        print(*spectrum, file=f)
        