from constant import CODON_TABLE
import re
import os

def get_data(file_suffix):
    current_directory = os.path.realpath(__file__).split('/')[-2]
    suffix = file_suffix.rstrip('.py').split('/')[-1].split('_')[-1].lower()
    file_path = f'data/{current_directory}/rosalind_{suffix}.txt'
    with open(file_path, 'r') as f:
        return f.read().strip()


def get_output_path(file_suffix):
    current_directory = os.path.realpath(__file__).split('/')[-2]
    suffix = file_suffix.rstrip('.py').split('/')[-1]
    file_path = f'./{current_directory}/output/{suffix}.txt'
    return file_path


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def reverse_complement(rna1):
    U = 'T' if 'T' in rna1 else 'U'

    rna2 = ''
    for char in rna1[::-1]:
        if char == 'A':
            rna2 += U
        elif char == U:
            rna2 += 'A'
        elif char == 'C':
            rna2 += 'G'
        elif char == 'G':
            rna2 += 'C'

    return rna2


def compare_with_selection(dna1, dna2, dna1_indexs, dna2_indexs):
    from rich import print as pprint
    str1 = dna1[:dna1_indexs[0]] + '[green]' + dna1[dna1_indexs[0]:dna1_indexs[1]] + '[/green]' + dna1[dna1_indexs[1]:]
    str2 = dna2[:dna2_indexs[0]] + '[green]' + dna2[dna2_indexs[0]:dna2_indexs[1]] + '[/green]' + dna2[dna2_indexs[1]:]
    
    pprint(str1)
    pprint(str2)


def rna_to_protein(rna, shift=0):
    seq = ''
    for i in range(shift, len(rna)-3+shift, 3):
        seq += CODON_TABLE[rna[i:i+3]]
                
    return seq


def rna_to_protein_strings(rna, shifts=True, include_reverse_complement=True, verbose=False):
    seqs = []

    for rna in [rna, reverse_complement(rna)] if include_reverse_complement else [rna]:
        for i in range(3 if shifts else 1):
            reading_frames = rna_to_protein(rna, shift=i)

            if verbose:
                print(reading_frames)

            if len(reading_frames) > 0:
                seqs.append(reading_frames)

    return seqs


def find_orf(protein_strings, pattern):
    orf = set()
    regex = re.compile(pattern)

    for seq in protein_strings:
        match = regex.findall(seq)

        for m in match:
            orf.add(m.rstrip('-'))
            sub_match = m

            if 'M' in sub_match[1:]:
                orf = orf.union(find_orf([sub_match[1:]], r'M.*?-'))

    return orf

