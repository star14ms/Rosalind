from util import get_data

data = get_data(__file__)
# data = '''>Rosalind_78
# PLEASANTLY
# >Rosalind_33
# MEANLY'''

data = data.split('>')[1:]
s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]


def get_augmented_str(s1_idx, s2_idx):
  if (s1_idx, s2_idx) in get_augmented_str.cache:
    return get_augmented_str.cache[(s1_idx, s2_idx)]
  
  if s1_idx == len(s1):
    return len(s2[s2_idx:]), 1
  
  if s2_idx == len(s2):
    return len(s1[s1_idx:]), 1
  
  augmented_strs = []

  # Assumming each first base is a match
  if s1[s1_idx] == s2[s2_idx]:
    edit_distance, n_alignments = get_augmented_str(s1_idx+1, s2_idx+1)
    augmented_strs.append((edit_distance, n_alignments))
  # Assumming substitution
  edit_distance, n_alignments = get_augmented_str(s1_idx+1, s2_idx+1)
  augmented_strs.append((edit_distance+1, n_alignments))
  # Assumming deletion
  edit_distance, n_alignments = get_augmented_str(s1_idx+1, s2_idx)
  augmented_strs.append((edit_distance+1, n_alignments))
  # Assumming insertion
  edit_distance, n_alignments = get_augmented_str(s1_idx, s2_idx+1)
  augmented_strs.append((edit_distance+1, n_alignments))

  # get the augmented string with the minimum edit distance
  min_edit_distance = float('inf')
  total_n_alignments = 0

  for edit_distance, n_alignments in augmented_strs:
    if edit_distance < min_edit_distance:
      min_edit_distance = edit_distance
      total_n_alignments = n_alignments
    elif edit_distance == min_edit_distance:
      total_n_alignments += n_alignments
      
  get_augmented_str.cache[(s1_idx, s2_idx)] = min_edit_distance, total_n_alignments
  return min_edit_distance, total_n_alignments % (2**27-1)


get_augmented_str.cache = {}
min_edit_distance, n_alignments = get_augmented_str(0, 0)
print(min_edit_distance, n_alignments)
