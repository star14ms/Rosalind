from util import get_data
from constant import get_alignment_score_one_unit

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
    return ('-' * len(s2[s2_idx:]), s2[s2_idx:]), -5 * len(s2[s2_idx:])
  
  if s2_idx == len(s2):
    return (s1[s1_idx:], '-' * len(s1[s1_idx:])), -5 * len(s1[s1_idx:])
  
  augmented_strs = []
  
  # Assumming each first base is a match
  if s1[s1_idx] == s2[s2_idx]:
    suffix, alignment_score = get_augmented_str(s1_idx+1, s2_idx+1)
    augmented_strs.append((s1[s1_idx] + suffix[0],
                           s2[s2_idx] + suffix[1], 
                           alignment_score + get_alignment_score_one_unit(s1[s1_idx], s2[s2_idx])))
  # Assumming substitution
  suffix, alignment_score = get_augmented_str(s1_idx+1, s2_idx+1)
  augmented_strs.append((s1[s1_idx] + suffix[0],
                         s2[s2_idx] + suffix[1], 
                         alignment_score + get_alignment_score_one_unit(s1[s1_idx], s2[s2_idx])))
  # Assumming deletion
  suffix, alignment_score = get_augmented_str(s1_idx+1, s2_idx)
  augmented_strs.append((s1[s1_idx] + suffix[0],
                         '-' + suffix[1], 
                         alignment_score - 5))
  # Assumming insertion
  suffix, alignment_score = get_augmented_str(s1_idx, s2_idx+1)
  augmented_strs.append(('-' + suffix[0],
                         s2[s2_idx] + suffix[1], 
                         alignment_score - 5))

  # get the augmented string with the minimum edit distance
  optimal_alignments = []
  maximum_alignment_score = float('-inf')

  for str1, str2, alignment_score in augmented_strs:
    if alignment_score > maximum_alignment_score:
      optimal_alignments = [(str1, str2)]
      maximum_alignment_score = alignment_score
    elif alignment_score == maximum_alignment_score:
      optimal_alignments.append((str1, str2))

  get_augmented_str.cache[(s1_idx, s2_idx)] = optimal_alignments[0], maximum_alignment_score
  return optimal_alignments[0], maximum_alignment_score


get_augmented_str.cache = {}
(augmented_str1, augmented_str2), maximum_alignment_score = get_augmented_str(0, 0)

print(augmented_str1, augmented_str2)
print(maximum_alignment_score)