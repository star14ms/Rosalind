from constant import CODON_TABLE
import re
import os
import subprocess
import Bio.Align.substitution_matrices.data as BioData


def get_filepath(file_suffix):
    current_directory = os.path.realpath(__file__).split('/')[-2]
    suffix = file_suffix.rstrip('.py').split('/')[-1].split('_')[-1].lower()
    file_path = f'data/{current_directory}/rosalind_{suffix}.txt'
    return file_path


def get_data(file_suffix):
    file_path = get_filepath(file_suffix)
    with open(file_path, 'r') as f:
        return f.read().strip()


def get_output_path(file_suffix, ext='txt'):
    current_directory = os.path.realpath(__file__).split('/')[-2]
    suffix = file_suffix.rstrip('.py').split('/')[-1]
    file_path = f'./{current_directory}/output/{suffix}.{ext}'
    return file_path


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_div(n, k):
    """Calculate n! / k! which simplifies the calculation avoiding large numbers."""
    result = 1
    for i in range(k + 1, n + 1):
        result *= i
    return result


def reverse_complement(rna1):
    U = 'U' if 'U' in rna1 else 'T'

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


def align_with_emboss(s1, s2, local=False, gapopen=10, gapextend=0.5, endweight=False, endopen=10, endextend=0.5, datafile='BLOSUM62', file_name='Align', verbose=False):
  command = 'matcher' if local else 'needle'

  for i, record in enumerate([s1, s2]):
    with open(get_output_path(f'{file_name}{i+1}', 'fasta'), 'w') as f:
      fasta = record.format("fasta")
      f.write(fasta)
      
  if '/' not in datafile:
      datafile = f"{BioData.__path__[0]}/{datafile}"

  subprocess.call([
    command, 
    "-datafile", datafile, 
    "-outfile", get_output_path(file_name, ext=command), 
    "-aformat3", "markx3", # Easy to read alignments
    "-gapopen", str(gapopen), 
    "-gapextend", str(gapextend), 
    "-auto", "false", 
    # "-alternatives", "30"
  ] + ([
    "-endweight", str(endweight),
    "-endopen", str(endopen),
    "-endextend", str(endextend),
  ] if not local else []) + [
    get_output_path(f'{file_name}1', ext='fasta'), 
    get_output_path(f'{file_name}2', ext='fasta')
  ], stderr=subprocess.DEVNULL if not verbose else None)

  with open(get_output_path(file_name, ext=command), 'r') as f:
    data = f.read()
    score = data[data.find('Score: ')+7:].split('\n')[0].split('.')[0]
    substring1 = data.split('> ..')[1].replace('\n', '')
    substring2 = data.split('> ..')[2].replace('\n', '').split('#')[0]

  return int(score), substring1, substring2
