### ChatGPT: https://chatgpt.com/share/c751994a-f4d3-4321-b100-fb515ea2e381
from util import get_data, get_output_path


def cyclopeptide_sequencing(spectrum):
    amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    peptides = {''}
    final_peptides = []

    def mass(peptide):
        return sum(map(int, peptide.split('-'))) if peptide else 0

    def cyclospectrum(peptide):
        peptide_masses = list(map(int, peptide.split('-')))
        n = len(peptide_masses)
        extended = peptide_masses + peptide_masses[:-1]
        spectrum = [0, sum(peptide_masses)]
        for l in range(1, n):
            for i in range(n):
                subpeptide_mass = sum(extended[i:i + l])
                spectrum.append(subpeptide_mass)
        return sorted(spectrum)

    parent_mass = max(spectrum)

    while peptides:
        # Expand peptides
        peptides = {f"{pep}-{m}" if pep else f"{m}" for pep in peptides for m in amino_acid_masses}
        
        # Check each peptide and remove inconsistent ones
        to_remove = set()
        for peptide in peptides:
            if mass(peptide) == parent_mass:
                if cyclospectrum(peptide) == spectrum:
                    final_peptides.append(peptide)
                to_remove.add(peptide)
            elif not all(any(m == sp for sp in spectrum) for m in cyclospectrum(peptide)):
                to_remove.add(peptide)
        
        peptides.difference_update(to_remove)

    return final_peptides


if __name__ == "__main__":
    # data = get_data('_40_BA4E.py')
    data ='''0 113 128 186 241 299 314 427'''
    print(data)
    
    spectrum = list(map(int, data.split()))
    output_peptides = cyclopeptide_sequencing(spectrum)
    
    print(len(output_peptides))
    # Print results
    with open(get_output_path(__file__), 'w') as f:
        for peptide in output_peptides:
            print(peptide, end=' ')
            print(peptide, end=' ', file=f)
    print()
