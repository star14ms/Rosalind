from util import get_data, get_output_path
from Bio.Align import PairwiseAligner


# data = get_data(__file__)
data = '''>Rosalind_92
AACGTA
>Rosalind_47Z
ACACCTA
'''

data = data.split('>')[1:]
s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]


def calculate_max_gaps(seq1, seq2):
    # Create an aligner object
    aligner = PairwiseAligner()
    
    # Set scoring
    aligner.match_score = 1    # Positive score for matches
    aligner.mismatch_score = -2    # Negative score for mismatches
    aligner.open_gap_score = -1    # Negative score for opening a gap
    aligner.extend_gap_score = -1  # Negative score for extending a gap
    
    # Calculate alignments
    alignments = aligner.align(seq1, seq2)
    
    # Find the alignment with the maximum number of gaps
    max_gaps = max(aln.counts().gaps for aln in alignments)
    
    return max_gaps


max_gaps = calculate_max_gaps(s1, s2)
print(max_gaps)
