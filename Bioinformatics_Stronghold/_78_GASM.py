from util import get_data, get_output_path, reverse_complement


data = get_data(__file__)
# data = '''AATCT
# TGTAA
# GATTA
# ACAGA'''

k_mers = data.split('\n')
cyclic_superstring = k_mers.pop(0)
n_no_progress = 0
min_sharing = len(k_mers[0])

while k_mers:
  k_mer = k_mers.pop(0)
  k_mer_complement = reverse_complement(k_mer)
  print(len(k_mers), len(cyclic_superstring), '     ', end='\r')

  additional_strings = []

  if k_mer in cyclic_superstring or k_mer_complement in cyclic_superstring:
    continue

  for i in range(len(cyclic_superstring), min_sharing, -1):
    if cyclic_superstring[:i] == k_mer[-i:]:
      additional_strings.append(k_mer[:-i] + cyclic_superstring)
    if cyclic_superstring[-i:] == k_mer[:i]:
      additional_strings.append(cyclic_superstring + k_mer[i:])
    if cyclic_superstring[:i] == k_mer_complement[-i:]:
      additional_strings.append(k_mer_complement[:-i] + cyclic_superstring)
    if cyclic_superstring[-i:] == k_mer_complement[:i]: 
      additional_strings.append(cyclic_superstring + k_mer_complement[i:])

  if additional_strings:
    cyclic_superstring = min(additional_strings)
  else:
      n_no_progress += 1
      k_mers.append(k_mer)

  if n_no_progress == len(k_mers):
    min_sharing -= 1
    n_no_progress = 0


repeating_superstring = None
for i in range(1, len(cyclic_superstring)):
  if cyclic_superstring[:i] == cyclic_superstring[-i:]:
    repeating_superstring = cyclic_superstring[:i]
    
if repeating_superstring:
  cyclic_superstring = cyclic_superstring[:-len(repeating_superstring)]

print()
print(cyclic_superstring)

with open(get_output_path(__file__), 'w') as f:
  f.write(cyclic_superstring)