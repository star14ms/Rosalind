from util import get_data, get_output_path, align_with_emboss


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
            if length_diff >= len(s1_suffix) * 3/2 or length_diff >= len(s2_prefix) * 3/2:
                continue
            
            file_name = __file__.split('/')[-1].rstrip('.py')
            max_score, substring1, substring2 = align_with_emboss(
                s1_suffix, s2_prefix, local=False, gapopen=2, gapextend=2, endweight=True, endopen=2, endextend=2,
                datafile='/Users/minseo/Documents/Github/_Bioinfo/Rosalind/data/substitution_matrices/TRANS', file_name=file_name
            )

            if max_score >= max_score_with_s1_suffix:
                max_score_with_s1_suffix = max_score
                score_increasing = True
            elif score_increasing and max_score - max_score_with_s1_suffix < -20: # increasing can happens after decreasing
                break

            if max_score < optimal_overlap_alignment_score:
                continue

            if max_score > optimal_overlap_alignment_score:
                optimal_overlap_alignments = [(substring1, substring2)]
                optimal_overlap_alignment_score = max_score
            else:
                optimal_overlap_alignments.append((substring1, substring2))

            # print(max_score)
            # print(substring1)
            # print(substring2)

        if max_score_with_s1_suffix - optimal_overlap_alignment_score < -32:
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
    
    score_best, optimal_overlap_alignments = find_optimal_overlap_alignments(s1, s2)

    for alignment in optimal_overlap_alignments:
        print(score_best)
        print(*alignment, sep='\n')

    with open(get_output_path(__file__), 'w') as f:
        print(score_best, file=f)
        print(*optimal_overlap_alignments[-1], sep='\n', file=f)
