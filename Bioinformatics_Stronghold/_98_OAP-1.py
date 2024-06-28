from util import get_data, get_output_path
from Bio.Align import PairwiseAligner, substitution_matrices
import numpy as np


def custom_substitution_matrix(new_matrix, base_matrix_name='TRANS'):
    matrix = substitution_matrices.load(base_matrix_name)
    assert matrix.shape == new_matrix.shape

    for i, alphabet1 in enumerate(['A', 'C', 'G', 'T']):
        for j, alphabet2 in enumerate(['A', 'C', 'G', 'T']):
            matrix[alphabet1, alphabet2] = new_matrix[i, j]
            
    return matrix
            

def find_optimal_overlap_alignments(s1, s2):
    optimal_overlap_alignment_score = -float('inf')
    optimal_overlap_alignments = []

    for idx_suffix in range(len(s1)-1-1, 0, -1):
        s1_suffix = s1[idx_suffix:]
        score_increasing = False
        max_score_with_s1_suffix = -float('inf')
    
        for idx_prefix in range(1, len(s2)):
            s2_prefix = s2[:idx_prefix]
            
            length_diff = abs(len(s1_suffix) - len(s2_prefix))
            if length_diff > len(s1_suffix) * 3/2 or length_diff > len(s2_prefix) * 3/2:
                continue

            alignments = list(aligner.align(s1_suffix, s2_prefix))
            max_score = int(max([alignment.score for alignment in alignments]))
            
            if max_score >= max_score_with_s1_suffix:
                max_score_with_s1_suffix = max_score
                score_increasing = True
            elif score_increasing and max_score - max_score_with_s1_suffix < -20: # increasing can happens after decreasing
                break

            if max_score < optimal_overlap_alignment_score:
                continue

            alignment = list(filter(lambda x: x.score == max_score, alignments))[0]
            target = ''.join(alignment.target[i] if i != -1 else '-' for i in alignment.indices[0])
            query = ''.join(alignment.query[i] if i != -1 else '-' for i in alignment.indices[1])
            
            if max_score > optimal_overlap_alignment_score:
                optimal_overlap_alignments = [(target, query)]
                optimal_overlap_alignment_score = max_score
            else:
                optimal_overlap_alignments.append((target, query))

            print(max_score)
            print(target)
            print(query)

        if max_score_with_s1_suffix - optimal_overlap_alignment_score < -24:
            break

        print(len(s1_suffix), max_score_with_s1_suffix)
    return optimal_overlap_alignment_score, optimal_overlap_alignments


if __name__ == '__main__':
    data = get_data('99_OAP.py')
#     data = '''>Rosalind_54
# CTAAGGGATTCCGGTAATTAGACAG
# >Rosalind_45
# ATAGACCATATGTCAGTGACTGTGTAA'''

    data = data.split('>')[1:]
    s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]

    aligner = PairwiseAligner(scoring=None)
    new_matrix = np.array([[ 1, -2, -2, -2],
                           [-2,  1, -2, -2],
                           [-2, -2,  1, -2],
                           [-2, -2, -2,  1]])
    
    aligner.substitution_matrix = custom_substitution_matrix(new_matrix, 'TRANS')
    aligner.open_gap_score = -2.0
    aligner.extend_gap_score = -2.0
    aligner.target_end_gap_score = -2.0
    aligner.query_end_gap_score = -2.0
    
    score_best1, optimal_overlap_alignments1 = find_optimal_overlap_alignments(s1, s2)
    score_best2, optimal_overlap_alignments2 = find_optimal_overlap_alignments(s2, s1)

    if score_best2 > score_best1:
        score_best = score_best2
        optimal_overlap_alignments = optimal_overlap_alignments2
    else:
        score_best = score_best1
        optimal_overlap_alignments = optimal_overlap_alignments1
            
    for alignment in optimal_overlap_alignments:
        print(score_best)
        print(*alignment, sep='\n')
    
    with open(get_output_path(__file__), 'w') as f:
        print(score_best, file=f)
        print(*optimal_overlap_alignments[-1], sep='\n', file=f)
        