from util import get_data, get_output_path, align_with_emboss
from Bio.Align import PairwiseAligner, substitution_matrices
import Bio.Align.substitution_matrices.data as BioData


data = get_data(__file__)
# data = '''>Rosalind_80
# MEANLYPRTEINSTRING
# >Rosalind_21
# PLEASANTLYEINSTEIN'''

data = data.split('>')[1:]
s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]


# cd ./Bioinformatics_Stronghold/output/
f'''
matcher \
  -gapopen 5 \
  -gapextend 5 \
  -datafile {BioData.__path__[0]}/PAM250 \
  -outfile 82_LOCA.needle \
  -aformat3 markx3 \
  82_LOCA1.fasta \
  82_LOCA2.fasta
'''
# cd ../..

file_name = __file__.split('/')[-1].rstrip('.py')
score, substring1, substring2 = align_with_emboss(s1, s2, rocal=True, gapopen=5, gapextend=5, datafile='PAM250', file_name=file_name)

print(score)
print(substring1)
print(substring2)
  
with open(get_output_path(__file__), 'w') as f:
  f.write(f'{score}\n{substring1}\n{substring2}')


# # Using Biopython ### TOO SLOW
# aligner = PairwiseAligner(scoring=None)
# aligner.substitution_matrix = substitution_matrices.load("PAM250")
# aligner.mode = 'local'
# aligner.open_gap_score = -5.0
# aligner.extend_gap_score = -5.0

# alignments = list(aligner.align(s1, s2))
# print("Number of alignments: %d" % len(alignments))

# max_score = max([alignment.score for alignment in alignments])

# for alignment in list(filter(lambda x: x.score == max_score, alignments))[:10]:
#   substrings = list(map(lambda x: x.replace('-',''), alignment))
#   # print(alignment)

#   print(alignment.score)
#   print(*substrings, sep='\n')
#   print()
