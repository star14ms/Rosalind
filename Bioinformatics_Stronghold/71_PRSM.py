from util import get_data
from constant import MONOISOTOPIC_MASS_TABLE

data = get_data(__file__)
# data = '''4
# GSDMQS
# VWICN
# IASWMQS
# PVSMGAD
# 445.17838
# 115.02694
# 186.07931
# 314.13789
# 317.1198
# 215.09061'''

n, data = data.split('\n', 1)
*protein_strings, multiset = data.split('\n', int(n))
multiset = list(map(float, multiset.split()))

max_multiplicity_overall = 0
protein_where_max_multiplicity = None

for protein_string in protein_strings:
  diff = []
  prefix_weight = 0
  suffix_weight = 0
  for i in range(len(protein_string)):
    prefix_weight += MONOISOTOPIC_MASS_TABLE[protein_string[i]]
    suffix_weight += MONOISOTOPIC_MASS_TABLE[protein_string[-i-1]]
    
    for weight_spec in multiset:
      diff.append(round(weight_spec-prefix_weight, 10))
      diff.append(round(weight_spec-suffix_weight, 10))

  # Largest Multiplicity
  max_multiplicity = max(diff.count(x) for x in diff)
  
  print(max_multiplicity)
  print(protein_string)
  
  if max_multiplicity_overall < max_multiplicity:
    max_multiplicity_overall = max_multiplicity
    protein_where_max_multiplicity = protein_string

print(max_multiplicity_overall)
print(protein_where_max_multiplicity)
