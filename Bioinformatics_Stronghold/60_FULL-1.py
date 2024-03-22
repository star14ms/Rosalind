from util import get_data, get_output_path
from constant import MONOISOTOPIC_MASS_TABLE

# data = get_data(__file__)
data = '''1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391
1221.7188991
1249.7250491
1377.8200091'''

masses = list(map(float, data.split('\n')))
parent_mass = masses.pop(0)

# # find pairs of masses that sum to the parent mass
# elements = set()
# pairs = []

# for mass1 in masses:
#   for mass2 in masses:
#     if mass1 != mass2 and mass1 not in elements and parent_mass - (mass1 + mass2) < 0.001:
#       elements = elements.union((mass1, mass2))
#       pairs.append(mass1)
#       break
    
# print(elements)


# monoisotopic_masses = [0] * (len(pairs)-1)
# for i in range(1, len(pairs)):
#     monoisotopic_masses[i-1] = pairs[i] - pairs[i-1]

# print(monoisotopic_masses)
# protein = ''
# for mass in monoisotopic_masses:
#     for key, value in MONOISOTOPIC_MASS_TABLE.items():
#         if abs(value - mass) < 0.001:
#             protein += key
#             break


# find pairs of masses that sum to the parent mass
elements = []
pairs = []
protein = ''
intervals = {}

for i in range(len(masses)):
  for j in range(i+1, len(masses)):
    if i != j and parent_mass - (masses[i] + masses[j]) < 0.001:
      for key, value in MONOISOTOPIC_MASS_TABLE.items():
        if abs(value - abs(masses[j] - masses[i])) < 0.001:
            print(key, masses[i], masses[j], abs(masses[j] - masses[i]))
            intervals[(masses[i], masses[j])] = key
            protein += key
            elements.append((masses[i], masses[j]))
            break

print(protein)
print(intervals)
intervals_long = {}
intervals_2 = intervals.copy()

while len(intervals) > 0:
  (mass1, mass2), key = intervals.popitem()
  merged = False

  while True:
    next_seq = list(filter(lambda mass_interval: mass_interval[0] == mass2, {**intervals_2}))
    if len(next_seq) > 0:
      intervals_2[(mass1, next_seq[0][1])] = \
        intervals_2[(mass1, next_seq[0][0])] + \
        intervals_2[(next_seq[0][0], next_seq[0][1])]
      mass2 = next_seq[0][1]
      merged = True
    else:
      if merged:
        intervals_long[(mass1, mass2)] = intervals_2[(mass1, mass2)]
      break

  # print(mass1, mass2, key)
  # print(intervals_long)
  # input()

print(intervals_long)

# protein = 'KEKEP'
# weight = 0
# for amino_acid in protein:
#     weight += MONOISOTOPIC_MASS_TABLE[amino_acid]
    
# print(weight)
# breakpoint()

# 992 + K + E + K = 1120 + E + K = 1249 + K = 1377.82 + K