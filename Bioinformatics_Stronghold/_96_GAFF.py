from util import get_data, get_output_path, align_with_emboss
from Bio.Align import PairwiseAligner, substitution_matrices


data = get_data(__file__)
# data = '''>Rosalind_49
# PRTEINS
# >Rosalind_47
# PRTWPSEIN'''


file_name = __file__.split('/')[-1].rstrip('.py')
data = data.split('>')[1:]
s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]

score, substring1, substring2 = align_with_emboss(
  s1, s2, 
  gapopen=11, gapextend=1, endweight=True, endopen=11, endextend=1, 
  file_name=file_name
)

with open(get_output_path(__file__), 'w') as f:
  print(f'{score}\n{substring1}\n{substring2}')
  print(f'{score}\n{substring1}\n{substring2}', file=f)

################################################################################################################################


# aligner = PairwiseAligner(scoring=None)
# aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
# aligner.open_gap_score = -11.0
# aligner.extend_gap_score = -1.0

# alignments = list(aligner.align(s1, s2))
# print("Number of alignments: %d" % len(alignments))

# max_score = max([alignment.score for alignment in alignments])

# for alignment in list(filter(lambda x: x.score == max_score, alignments))[:10]:
#   target = ''.join(alignment.target[i] if i != -1 else '-' for i in alignment.indices[0])
#   query = ''.join(alignment.query[i] if i != -1 else '-' for i in alignment.indices[1])
#   print(alignment.score)
#   print(target)
#   print(query)