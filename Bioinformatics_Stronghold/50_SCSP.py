from util import get_data

data = get_data(__file__)
# data = '''ATCTGAT
# TGCATA'''
dna1, dna2 = data.split('\n')

def get_scs(idx1, idx2):
  '''Returns the shortest common supersequence of dna1 and dna2.'''
  global dna1, dna2

  if (idx1, idx2) in get_scs.cache:
    return get_scs.cache[(idx1, idx2)]

  if idx1 == len(dna1):
    get_scs.cache[(idx1, idx2)] = dna2[idx2:]
    return dna2[idx2:]
  elif idx2 == len(dna2):
    get_scs.cache[(idx1, idx2)] = dna1[idx1:]
    return dna1[idx1:]

  cs = []
  # skip the current base in dna1
  if dna1[idx1] != dna2[idx2]:
    common_superseq = dna2[idx2] + get_scs(idx1, idx2+1)
    cs.append(common_superseq)
    common_superseq = dna1[idx1] + get_scs(idx1+1, idx2)
    cs.append(common_superseq)

  # include the current base in dna1
  if dna1[idx1] in dna2[idx2:]:
    idx2_new = dna2.index(dna1[idx1], idx2)
    common_superseq = dna2[idx2:idx2_new+1] + get_scs(idx1+1, idx2_new+1)
    cs.append(common_superseq)
  if dna2[idx2] in dna1[idx1:]:
    idx1_new = dna1.index(dna2[idx2], idx1)
    common_superseq = dna1[idx1:idx1_new+1] + get_scs(idx1_new+1, idx2+1)
    cs.append(common_superseq)

  scs = min(cs, key=len)
  get_scs.cache[(idx1, idx2)] = scs
  return scs

get_scs.cache = {}
scs = get_scs(0, 0)
print(scs)

# for key, value in get_scs.cache.items():
#   dna1_sub = '' if len(dna1) == key[0] else dna1[key[0]:]
#   dna2_sub = '' if len(dna2) == key[1] else dna2[key[1]:]
#   print(dna1_sub, dna2_sub, value)
  
# print(len(get_scs.cache))