from util import get_data

data = get_data(__file__)
# data = '''ATTAC
# TACAG
# GATTA
# ACAGA
# CAGAT
# TTACA
# AGATT'''

k_mers = data.split('\n')
cyclic_superstring = k_mers.pop(0)
n_no_progress = 0
min_sharing = len(k_mers[0])

while k_mers:
  k_mer = k_mers.pop(0)
  print(len(k_mers), len(cyclic_superstring), '     ', end='\r')

  additional_strings = []

  if k_mer in cyclic_superstring:
    continue

  for i in range(len(cyclic_superstring), min_sharing, -1):
    if cyclic_superstring[:i] == k_mer[-i:]:
      additional_strings.append(k_mer[:-i] + cyclic_superstring)
    if cyclic_superstring[-i:] == k_mer[:i]:
      additional_strings.append(cyclic_superstring + k_mer[i:])

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

print()
print(cyclic_superstring[:-len(repeating_superstring)])
