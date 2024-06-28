from util import get_data, get_output_path, align_with_emboss


if __name__ == '__main__':
    data = get_data(__file__)
#     data = '''>Rosalind_79
# CAGCACTTGGATTCTCGG
# >Rosalind_98
# CAGCGTGG'''

    data = data.split('>')[1:]
    seq, motif = [x.split('\n', 1)[1].replace('\n', '') for x in data]   

    file_name = __file__.split('/')[-1].rstrip('.py')

    score, substring1, substring2 = align_with_emboss(
        seq, motif, 
        local=False, gapopen=1, gapextend=1, 
        endweight=False, endopen=1, endextend=1,
        datafile='/Users/minseo/Documents/Github/_Bioinfo/Rosalind/data/substitution_matrices/ONES',
        file_name=file_name
    )

    print(score)
    print(substring1)
    print(substring2)
    
    with open(get_output_path(__file__), 'w') as f:
        print(score, substring1, substring2, sep='\n', file=f)
