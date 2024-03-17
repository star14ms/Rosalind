from util import get_data, get_output_path

data = get_data(__file__)
# data = '''>Rosalind_23
# AACCTTGG
# >Rosalind_64
# ACACTGTGA'''
data = data.split('>')[1:]
dna1, dna2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]

# find the longest common subsequences
subsequence_dict = {}

def get_longest_common_subsequences(dna1_index, dna2_index):
  if (dna1_index, dna2_index) in subsequence_dict:
    return subsequence_dict[(dna1_index, dna2_index)]
  
  def search_next_subsequence_unit(dna1_index, dna2_index):
    result = {}
    for base in ['A', 'C', 'T', 'G']:
      if base in dna1[dna1_index:] and base in dna2[dna2_index:]:
        dna1_index_new = dna1.index(base, dna1_index)
        dna2_index_new = dna2.index(base, dna2_index)
        distance = (dna1_index_new - dna1_index) + (dna2_index_new - dna2_index)
        result[base] = distance
        
    return result

  result = search_next_subsequence_unit(dna1_index, dna2_index)

  if not result:
    return ['']

  subsequence_list = []
  for base in result:
    dna1_index_new = dna1.index(base, dna1_index)
    dna2_index_new = dna2.index(base, dna2_index)
    subsequences = get_longest_common_subsequences(dna1_index_new+1, dna2_index_new+1)
    subsequence_dict[(dna1_index_new+1, dna2_index_new+1)] = subsequences
    
    for subsequence in subsequences:
      subsequence_list.append(base + subsequence)

  longest_length = len(max(subsequence_list, key=len))
  subsequences_longest = [subsequence for subsequence in subsequence_list if len(subsequence) == longest_length]
  return subsequences_longest


def get_longest_common_subsequence(dna1_index, dna2_index):
  global subsequence_dict, dna1, dna2

  if (dna1_index, dna2_index) in subsequence_dict:
    return subsequence_dict[(dna1_index, dna2_index)]
  
  def search_next_subsequence_unit(dna1_index, dna2_index):
    result = {}
    for base in ['A', 'C', 'T', 'G']:
      if base in dna1[dna1_index:] and base in dna2[dna2_index:]:
        dna1_index_new = dna1.index(base, dna1_index)
        dna2_index_new = dna2.index(base, dna2_index)
        distance = (dna1_index_new - dna1_index) + (dna2_index_new - dna2_index)
        result[base] = distance
        
    return result

  result = search_next_subsequence_unit(dna1_index, dna2_index)

  if not result:
    return ''

  subsequence_list = []
  for base in result:
    dna1_index_new = dna1.index(base, dna1_index)
    dna2_index_new = dna2.index(base, dna2_index)
    subsequence = get_longest_common_subsequence(dna1_index_new+1, dna2_index_new+1)
    subsequence_dict[(dna1_index_new+1, dna2_index_new+1)] = subsequence
    subsequence_list.append(base + subsequence)

  subsequence_longest = max(subsequence_list, key=len)
  return subsequence_longest


longest_common_subsequences = get_longest_common_subsequence(0, 0)
print(longest_common_subsequences)
