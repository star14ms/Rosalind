from util import get_data, get_output_path, align_with_emboss
from tqdm import tqdm


def find_all_similar_motifs(genome, motif, k):
    """
    Finds possible substrings in the genome that have an edit distance less than or equal to k with the given motif.

    Args:
        k (int): The maximum allowed edit distance.
        motif (str): The motif to search for in the genome.
        genome (str): The genome sequence.

    Returns:
        list: A list of tuples representing the possible substrings found. Each tuple contains the start position and length of the substring.
    """
    file_name = __file__.split('/')[-1].rstrip('.py')

    score, substring1, substring2 = align_with_emboss(
        genome, motif, 
        local=False, gapopen=5, gapextend=1,
        endweight=True, endopen=1, endextend=1,
        datafile='/Users/minseo/Documents/Github/_Bioinfo/Rosalind/data/substitution_matrices/ONES',
        file_name=file_name
    )
    
    with open(get_output_path(__file__), 'w') as f:
        print(substring1, file=f)
        print(substring2, file=f)

    idx_end_gap_left = len(substring2) - len(substring2.lstrip('-'))
    idx_end_gap_right = len(substring2.rstrip('-'))
    
    idx_lstriped = max(idx_end_gap_left-k, 0)
    idx_rstriped = min(idx_end_gap_right+k, len(substring1))
    genome = substring1[idx_lstriped:idx_rstriped]
    # print(substring1[idx_lstriped:idx_rstriped])
    # print(substring2[idx_lstriped:idx_rstriped])

    possible_substrings = []
    min_distance = 0
    n_run_emboss = 0
    
    def f(start, length):
        substring = genome[start-idx_lstriped:start-idx_lstriped+length]
        score, _, _ = align_with_emboss(
            substring, motif, 
            local=False, gapopen=1, gapextend=1, 
            endweight=True, endopen=1, endextend=1,
            datafile='/Users/minseo/Documents/Github/_Bioinfo/Rosalind/data/substitution_matrices/ZEROS',
            file_name=file_name, verbose=False,
        )
        edit_distance = -score
        
        return edit_distance
        
    # breakpoint()

    for length in (pbar := tqdm(range(len(motif)-k, len(motif)+k+1))):
        pbar.set_description(f"Length {length} ({length-(len(motif)-k)}/{k*2})")
        
        if min_distance - k > 0:
            min_distance -= 1
            continue

        min_distance = float('inf')
        n_to_jump = 0

        for start in range(len(genome) - length + 1):
            if n_to_jump > 0:
                print(idx_lstriped+start+1, length, n_to_jump)
                n_to_jump -= 2
                continue
            if (idx_lstriped+start+1, length) in possible_substrings:
                continue

            substring = genome[start:start+length]

            score, _, _ = align_with_emboss(
                substring, motif, 
                local=False, gapopen=1, gapextend=1, 
                endweight=True, endopen=1, endextend=1,
                datafile='/Users/minseo/Documents/Github/_Bioinfo/Rosalind/data/substitution_matrices/ZEROS',
                file_name=file_name, verbose=False,
            )
            edit_distance = -score

            if edit_distance <= k:
                possible_substrings.append((idx_lstriped+start+1, length))
                print((idx_lstriped+start+1, length))

                extra_length = 0
                while edit_distance + extra_length < k:
                    extra_length += 1
                    possible_substrings.append((idx_lstriped+start+1, length+extra_length))
                    print((idx_lstriped+start+1, length))
            else:
                # Logic error: 
                # If I jump n_to_jump, I will miss the next substring that has edit distance less than k
                n_to_jump = edit_distance - k
                
            print(edit_distance, n_to_jump, (idx_lstriped+start+1, length))
            
            if edit_distance < min_distance:
                min_distance = edit_distance
        
            n_run_emboss += 1

    print(n_run_emboss)
    
    
    # len_motif = 5000
    # len_seq = 50000
    # k = 50
    # n_run_emboss = sum([(len_seq - length + 1) for length in range((len_motif - k) // 2, 2*len_motif+k+1)])
    # print(n_run_emboss)
    # n_run_emboss = sum([(len_seq - length + 1) for length in range(len_motif-k, len_motif+k+1)])
    # print(n_run_emboss)

    return possible_substrings
    

if __name__ == '__main__':
    data = get_data(__file__)
#     data = '''2
# ACGTAG
# ACGGATCGGCATCGT'''

    k, motif, genome = data.split('\n')

    possible_substrings = find_all_similar_motifs(genome, motif, int(k))
    
    with open(get_output_path(__file__), 'w') as f:
        for possible_substring in possible_substrings:
            print(*possible_substring, sep=' ')
            print(*possible_substring, sep=' ', file=f)
        