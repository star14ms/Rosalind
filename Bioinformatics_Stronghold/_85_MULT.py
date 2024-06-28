### imperfect solution
from util import get_data, get_output_path
from Bio.Align import PairwiseAligner
from rich import print as pprint


def align(seq1, seq2, match_score=0, mismatch_score=-1, open_gap_score=-1, extend_gap_score=-1):
    # Create an aligner object
    aligner = PairwiseAligner()
    
    # Set scoring
    aligner.match_score = match_score    # Positive score for matches
    aligner.mismatch_score = mismatch_score    # Negative score for mismatches
    aligner.open_gap_score = open_gap_score    # Negative score for opening a gap
    aligner.extend_gap_score = extend_gap_score  # Negative score for extending a gap
    
    # Calculate alignments
    alignments = aligner.align(seq1, seq2)
    
    target_aligned_list = {}
    query_aligned_list = {}
    
    for aln in alignments:
        target = ''.join(aln.target[i] if i != -1 else '-' for i in aln.indices[0])
        query = ''.join(aln.query[i] if i != -1 else '-' for i in aln.indices[1])
        # print(aln.score)
        # print(target)
        # print(query)
        
        if target not in target_aligned_list:
            target_aligned_list[target] = [1, aln.score]
        else:
            target_aligned_list[target][0] += 1
            target_aligned_list[target][1] += aln.score

        if query not in query_aligned_list:
            query_aligned_list[query] = [1, aln.score]
        else:
            query_aligned_list[query][0] += 1
            query_aligned_list[query][1] += aln.score
    
    for key, value in target_aligned_list.items():
        target_aligned_list[key] = value[1] / value[0]
    for key, value in query_aligned_list.items():
        query_aligned_list[key] = value[1] / value[0]
        
    # print(target_aligned_list)
    # print(query_aligned_list)
    
    return target_aligned_list, query_aligned_list


def colorize_alignment(sequences, index, color):
    sequences = [
        sequence[:index] + f'[{color}]' + sequence[index] + f'[/{color}]' + sequence[index+1:] \
        for sequence in sequences
    ]
    
    return sequences


def score_MSA(alignment):
    aligns_formatted = alignment
    score = 0
    for i in range(len(alignment[0])-1, -1, -1):
        if alignment[0][i] == alignment[1][i] == alignment[2][i] == alignment[3][i]:
            aligns_formatted = colorize_alignment(aligns_formatted, i, 'green')
        else:
            n_same = max(
                [alignment[0][i], alignment[1][i], alignment[2][i], alignment[3][i]].count(char) \
                for char in [alignment[0][i], alignment[1][i], alignment[2][i], alignment[3][i]]
            )
            n_kind = len(set([alignment[0][i], alignment[1][i], alignment[2][i], alignment[3][i]]))

            if n_kind == 2 and n_same == 3:
                aligns_formatted = colorize_alignment(aligns_formatted, i, 'yellow')
                score -= 3
            elif n_kind == 2 and n_same == 2:
                aligns_formatted = colorize_alignment(aligns_formatted, i, 'orange1')
                score -= 4
            elif n_kind == 3:
                aligns_formatted = colorize_alignment(aligns_formatted, i, 'red')
                score -= 5
            else:
                aligns_formatted = colorize_alignment(aligns_formatted, i, 'grey0')
                score -= 6

    return score, aligns_formatted


def get_scores_of_all_combinations_of_alignments(seqs):
    comb_aligned_dict = {}

    for seq in seqs:
        comb_aligned_dict[seq] = dict()

    for i in range(len(seqs)):
        for j in range(i+1, len(seqs)):
            target_aligned, query_aligned = align(seqs[i], seqs[j])

            for seq, score in target_aligned.items():
                if comb_aligned_dict[seqs[i]].get(seq):
                    comb_aligned_dict[seqs[i]][seq][0] += 1
                    comb_aligned_dict[seqs[i]][seq][1] += score
                else:
                    comb_aligned_dict[seqs[i]][seq] = [1, score]
                    
            for seq, score in query_aligned.items():
                if comb_aligned_dict[seqs[j]].get(seq):
                    comb_aligned_dict[seqs[j]][seq][0] += 1
                    comb_aligned_dict[seqs[j]][seq][1] += score
                else:
                    comb_aligned_dict[seqs[j]][seq] = [1, score]

    for seq, gapped_seqs_dict in comb_aligned_dict.items():
        for gapped_seq, (n_times, score_total) in gapped_seqs_dict.items():
            comb_aligned_dict[seq][gapped_seq] = score_total / n_times

    return comb_aligned_dict


def get_new_seqs(seqs, comb_aligned_dict):
    seqs_best_dict = {}
    for seq in seqs:
        seqs_best_dict[seq] = [seq]
    
    best_score_average = -float('inf')
    for seq, aligned_dict in comb_aligned_dict.items():
        for seq_gapped, score_average in aligned_dict.items():
            if score_average > best_score_average and seq_gapped not in seqs:
                seqs_best_dict[seq] = [seq_gapped]
                best_score_average = score_average
            elif score_average == best_score_average and seq_gapped not in seqs:
                seqs_best_dict[seq].append(seq_gapped)

    new_seqs_list = []

    def _build_all_combinations_of_seqences(alignments=[]):
        nonlocal new_seqs_list

        if len(alignments) == len(seqs_best_dict):
            new_seqs_list.append(alignments)
            return

        for alignment in list(seqs_best_dict.values())[len(alignments)]:
            _build_all_combinations_of_seqences(alignments + [alignment])
            
    _build_all_combinations_of_seqences()
    
    return new_seqs_list


def get_MSA_best_score(comb_aligned_dict):    
    aligned_dict_simple = {}
    for seq, gapped_seqs_dict in comb_aligned_dict.items():
        aligned_dict_simple[seq] = list(gapped_seqs_dict.keys())

    max_score = -float('inf')
    best_alignments = []
    best_alignments_formatted = []

    def _get_MSA_best_score(alignments=[]):
        nonlocal max_score, best_alignments, best_alignments_formatted

        if len(alignments) == len(aligned_dict_simple):
            score, aligns_formatted = score_MSA(alignments)
            
            if score > max_score:
                max_score = score
                best_alignments = [alignments]
                best_alignments_formatted = [aligns_formatted]
            elif score == max_score:
                best_alignments.append(alignments)
                best_alignments_formatted.append(aligns_formatted)
            return

        for alignment in list(aligned_dict_simple.values())[len(alignments)]:
            if len(alignments) > 0 and len(alignment) != len(alignments[0]):
                continue

            _get_MSA_best_score(alignments + [alignment])

    _get_MSA_best_score()
    
    if len(best_alignments) == 0:
        print('No multiple sequence alignment found')

    return max_score, best_alignments, best_alignments_formatted


if __name__ == '__main__':
    data = get_data(__file__)
    data = '''>Rosalind_7
ATATCCG
>Rosalind_35
TCCG
>Rosalind_23
ATGTACTG
>Rosalind_44
ATGTCTG'''

    fastas = data.split('>')[1:]
    seqs = [fasta.split('\n', 1)[1].replace('\n', '') for fasta in fastas]
    # print(*seqs, sep='\n')
    # print([len(seq) for seq in seqs])

    comb_aligned_dict = get_scores_of_all_combinations_of_alignments(seqs)
    best_score, MSA_best, MSA_best_formatted = get_MSA_best_score(comb_aligned_dict)
    seqs_news = [(seqs, comb_aligned_dict, MSA_best, MSA_best_formatted)]

    while seqs_news:
        seqs, comb_aligned_dict, _, _ = seqs_news.pop()
        seqs_new_list = get_new_seqs(seqs, comb_aligned_dict)
        score_renewed = False

        for seqs_new_yet in seqs_new_list:
            new_comb_aligned_dict = get_scores_of_all_combinations_of_alignments(seqs_new_yet)
            new_best_score, new_MSA_best, new_MSA_best_formatted = get_MSA_best_score(new_comb_aligned_dict)

            if new_best_score > best_score:
                best_score = new_best_score
                seqs_news = [(seqs_new_yet, new_comb_aligned_dict, new_MSA_best, new_MSA_best_formatted)]
                score_renewed = True
            elif new_best_score == best_score and score_renewed:
                seqs_news += [(seqs_new_yet, new_comb_aligned_dict, new_MSA_best, new_MSA_best_formatted)]

        for (_, _, _, MSA_best_formatted) in seqs_news:
            for MSA_formatted in MSA_best_formatted:
                print(best_score)
                for alignment in MSA_formatted:
                    pprint(alignment)
        print('-' * 32)

    for MSA in MSA_best:
        print(best_score)
        for alignment in MSA:
            pprint(alignment)

# score, aligns_formatted = score_MSA([
#     'GATTCAGTGA',
#     'AGCGCTCGAC',
#     'CAGAATATAG',
#     '--AGGGCGCC',
# ])

# print(score)
# pprint(*aligns_formatted, sep='\n')


