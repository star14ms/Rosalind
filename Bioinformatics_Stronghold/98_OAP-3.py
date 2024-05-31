from util import get_data, get_output_path, align_with_emboss


def find_optimal_overlap_alignments(s1, s2):
    file_name = __file__.split('/')[-1].rstrip('.py')
    max_score, substring1, substring2 = align_with_emboss(
        s1, s2, local=True, gapopen=2, gapextend=2, endweight=True, endopen=2, endextend=2,
        datafile='/Users/minseo/Documents/Github/_Bioinfo/Rosalind/data/substitution_matrices/TRANS', file_name=file_name
    )

    return max_score, [(substring1, substring2)]


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
        # print(*alignment, sep='\n')

    with open(get_output_path(__file__), 'w') as f:
        print(score_best, file=f)
        print(*optimal_overlap_alignments[-1], sep='\n', file=f)
        
    substring1 = optimal_overlap_alignments[0][0].replace('-', '')
    
    index1 = s1.index(substring1)
    print(index1, len(s1))
