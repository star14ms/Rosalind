from util import get_data

data = get_data(__file__)
# data = '''>Rosalind_57
# AUAU'''
rna = data.split('\n', 1)[1].replace('\n', '')


def motzkin_number(seq):
  if len(seq) <= 1:
    return 1
  
  if seq in motzkin_number.cache:
    return motzkin_number.cache[seq]
  
  result = motzkin_number(seq[1:])
  
  for i in range(1, len(seq)):
    if (seq[0], seq[i]) in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]:
      result += motzkin_number(seq[1:i]) * motzkin_number(seq[i+1:])
  
  motzkin_number.cache[seq] = result
  
  return result


motzkin_number.cache = {}
print(motzkin_number(rna) % 1000000)
print(motzkin_number.cache)