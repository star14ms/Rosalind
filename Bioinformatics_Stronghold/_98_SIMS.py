from util import get_data, get_output_path, align_with_emboss


def score_alignment(seq1, seq2):
    score = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            score += 1
        else:
            score -= 1

    return score


if __name__ == '__main__':
    data = get_data(__file__)
#     data = '''>Rosalind_54
# GCAAACCATAAGCCCTACGTGCCGCCTGTTTAAACTCGCGAACTGAATCTTCTGCTTCACGGTGAAAGTACCACAATGGTATCACACCCCAAGGAAAC
# >Rosalind_46
# GCCGTCAGGCTGGTGTCCG'''

    data = data.split('>')[1:]
    seq, motif = [x.split('\n', 1)[1].replace('\n', '') for x in data]   

    file_name = __file__.split('/')[-1].rstrip('.py')

    score, substring1, substring2 = align_with_emboss(
        seq, motif, 
        local=True, gapopen=1, gapextend=1, 
        endweight=True, endopen=1, endextend=1,
        datafile='/Users/minseo/Documents/Github/_Bioinfo/Rosalind/data/substitution_matrices/ONES',
        file_name=file_name
    )

    prefix1, suffix1 = seq.split(substring1.replace('-', ''), 1)
    prefix2, suffix2 = motif.split(substring2.replace('-', ''), 1)
    
    if len(substring2.replace('-', '')) != len(motif):
        substring1 = prefix1[-len(prefix2):] + substring1 + suffix1[:len(suffix2)]
        substring2 = prefix2 + substring2 + suffix2
        score = score_alignment(substring1, substring2)
    
    with open(get_output_path(__file__), 'w') as f:
        print(score, substring1, substring2, sep='\n')
        print(score, substring1, substring2, sep='\n', file=f)
