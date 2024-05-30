from util import get_data

rna = get_data(__file__)
# rna = '''AUGCUAGUACGGAGCGAGUCUAGCGAGCGAUGUCGUGAGUACUAUAUAUGCGCAUAAGCCACGU'''

def motzkin_number(seq):
  if len(seq) <= 1:
    return 1
  
  if seq in motzkin_number.cache:
    return motzkin_number.cache[seq]
  
  result = motzkin_number(seq[1:])
  
  for i in range(1, len(seq)):
    if (seq[0], seq[i]) in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C'), ('G', 'U'), ('U', 'G')] and i >= 4:
      result += motzkin_number(seq[1:i]) * motzkin_number(seq[i+1:])
  
  motzkin_number.cache[seq] = result
  
  return result


motzkin_number.cache = {}
print(motzkin_number(rna))
