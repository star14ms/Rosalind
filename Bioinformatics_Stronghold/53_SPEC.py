from util import get_data
from constant import MONOISOTOPIC_MASS_TABLE

data = get_data(__file__)
# data ='''3524.8542
# 3710.9335
# 3841.974
# 3970.0326
# 4057.0646'''

prefix_weights = list(map(float, data.split('\n')))

monoisotopic_masses = [0] * (len(prefix_weights)-1)
for i in range(1, len(prefix_weights)):
    monoisotopic_masses[i-1] = prefix_weights[i] - prefix_weights[i-1]

protein = ''
for mass in monoisotopic_masses:
    for key, value in MONOISOTOPIC_MASS_TABLE.items():
        if abs(value - mass) < 0.001:
            protein += key
            break

print(protein)