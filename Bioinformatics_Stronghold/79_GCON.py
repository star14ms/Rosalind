from util import get_data
from Bio.Align import PairwiseAligner, substitution_matrices


data = get_data(__file__)
# data = '''>Rosalind_79
# PLEASANTLY
# >Rosalind_41
# MEANLY'''

data = data.split('>')[1:]
s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]

aligner = PairwiseAligner(scoring=None)
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -5.0
aligner.extend_gap_score = 0


alignments = list(aligner.align(s1, s2))
print("Number of alignments: %d" % len(alignments))

max_score = max([alignment.score for alignment in alignments])

# # count number of alignments with max score
# print("Number of alignments with max score: %d" % len(list(filter(lambda x: x.score == max_score, alignments))))

for alignment in list(filter(lambda x: x.score == max_score, alignments))[:10]:
  print("Score = %.1f:" % alignment.score)
  print(alignment)
