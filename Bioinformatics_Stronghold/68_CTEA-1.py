from util import get_data

data = get_data('68_CTEA.py')
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
    return ('-' * len(s2[s2_idx:]), s2[s2_idx:]), 1
  
  if s2_idx == len(s2):
    return (s1[s1_idx:], '-' * len(s1[s1_idx:])), 1
  
  augmented_strs = []
  
  # Assumming substitution
  suffix, n_alignments = get_augmented_str(s1_idx+1, s2_idx+1)
  augmented_strs.append((s1[s1_idx] + suffix[0], \
                         s2[s2_idx] + suffix[1], n_alignments))
  # Assumming deletion
  suffix, n_alignments = get_augmented_str(s1_idx+1, s2_idx)
  augmented_strs.append((s1[s1_idx] + suffix[0], \
                         '-' + suffix[1], n_alignments))
  # Assumming insertion
  suffix, n_alignments = get_augmented_str(s1_idx, s2_idx+1)
  augmented_strs.append(('-' + suffix[0], \
                         s2[s2_idx] + suffix[1], n_alignments))

  # get the augmented string with the minimum edit distance
  max_n_matching = -1
  min_edit_distance = float('inf')
  optimal_alignments = []
  total_n_alignments = 0

  for str1, str2, n_alignments in augmented_strs:
    n_matching = sum([1 for i in range(len(str1)) if str1[i] == str2[i]])
    edit_distance = sum([1 for i in range(len(str1)) if str1[i] != str2[i]])

    if edit_distance < min_edit_distance or (edit_distance == min_edit_distance and n_matching > max_n_matching):
      min_edit_distance = edit_distance
      max_n_matching = n_matching
      optimal_alignments = [(str1, str2)]
      total_n_alignments = n_alignments
    elif edit_distance == min_edit_distance and n_matching == max_n_matching:
      optimal_alignments.append((str1, str2))
      total_n_alignments += n_alignments
      
  get_augmented_str.cache[(s1_idx, s2_idx)] = optimal_alignments[-1][:2], total_n_alignments
  return optimal_alignments[-1][:2], total_n_alignments


get_augmented_str.cache = {}
(augmented_str1, augmented_str2), n_alignments = get_augmented_str(0, 0)

edit_distance = sum([1 for i in range(len(augmented_str1)) if augmented_str1[i] != augmented_str2[i]])
print(edit_distance, n_alignments)
