### hard
from util import get_data, get_output_path, compare_with_selection

data = get_data(__file__)

fastas = data.split('>')[1:]
dnas = [fasta.split('\n', 1)[1].replace('\n', '') for fasta in fastas]

def get_shortest_common_supersequence(s1, s2, len_minimum_subsequence=3*200):
  '''a shortest common supersequence is a string that contains every string in the list as a subsequence'''
  len_min = len_minimum_subsequence

  if s1[-len_min:] in s2:
    len_subseq = s2.index(s1[-len_min:]) + len_min
    # compare_with_selection(s1, s2, (-len_subseq, len(s1)), (0, len_subseq))
    # breakpoint()
    if s2[:len_subseq] in s1:
      return s1 + s2[len_subseq:]

  if s2[-len_min:] in s1:
    len_subseq = s1.index(s2[-len_min:]) + len_min
    # compare_with_selection(s2, s1, (-len_subseq, len(s2)), (0, len_subseq))
    # breakpoint()
    if s1[:len_subseq+1] in s2:
      return s2 + s1[len_subseq:]

  return False


merged_sequences = dnas
len_minimum_subsequence = len(dnas[0]) * 2 // 3
n_fail = 0
i = 0

while len(merged_sequences) > 1:
  i += 1
  shortest_common_supersequence = \
    get_shortest_common_supersequence(merged_sequences[0], merged_sequences[1], len_minimum_subsequence)
  if isinstance(shortest_common_supersequence, str):
    merged_sequences = [shortest_common_supersequence] + merged_sequences[2:]
    print(len(merged_sequences), 'seqs left,', 'len superstring:', len(shortest_common_supersequence), 'len minimum subsequence:', len_minimum_subsequence)
  else:
    n_fail += 1
    if not n_fail > len(merged_sequences):
      merged_sequences = [merged_sequences[0]] + merged_sequences[2:] + [merged_sequences[1]]
    else:
      merged_sequences = merged_sequences[1:] + [merged_sequences[0]]
      len_minimum_subsequence -= 3
      n_fail = 0
      if len_minimum_subsequence < 1:
        print('failed to merge sequences')
        break

print(i)
# print(shortest_common_supersequence)


with open(get_output_path(__file__), 'w') as output_data:
  output_data.write(shortest_common_supersequence + '\n')