from util import get_data
from constant import MONOISOTOPIC_MASS_TABLE

seq = get_data(__file__)

mass = 0
for aa in seq:
    mass += MONOISOTOPIC_MASS_TABLE[aa]

print(mass)
