from util import get_data
from constant import MONOISOTOPIC_MASS_TABLE

data = get_data(__file__)
# data = '''3524.8542
# 3623.5245
# 3710.9335
# 3841.974
# 3929.00603
# 3970.0326
# 4026.05879
# 4057.0646
# 4083.08025'''


masses = list(map(float, data.split('\n')))


def find_amino_acid_by_mass(mass_diff, tolerance=0.01):
    for aa, mass in MONOISOTOPIC_MASS_TABLE.items():
        if abs(mass - mass_diff) <= tolerance:
            return aa
    return None


queue = [(0, '', i) for i in range(len(masses))]
longest_protein_string = ''

while queue:
    previous_diff, protein_string, start_index = queue.pop(0)
  
    for i in range(start_index, len(masses)-1):
        mass_diff = masses[i+1] - masses[i]
        amino_acid = find_amino_acid_by_mass(mass_diff + previous_diff)
  
        if amino_acid:
            queue.append((mass_diff + previous_diff, protein_string, start_index+1))
            protein_string += amino_acid
            previous_diff = 0
        else:
            previous_diff += mass_diff

    if len(protein_string) > len(longest_protein_string) and previous_diff == 0:
        longest_protein_string = protein_string

print(longest_protein_string)
