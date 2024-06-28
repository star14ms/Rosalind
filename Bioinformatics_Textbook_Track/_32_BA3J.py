from util import get_data, get_output_path


def read_paired_kmers(paired_kmers_str):
    return [paired_kmer_str.split('|') for paired_kmer_str in paired_kmers_str]


def reconstruct_string_from_paired_kmers(paired_kmers, distance):
    text1, text2 = paired_kmers.pop(0)
    k = len(text1)

    while len(paired_kmers):
        paired_kmer = paired_kmers.pop(0)
        kmer1, kmer2 = paired_kmer
        
        if text1[:k-1] == kmer1[1:] and text2[:k-1] == kmer2[1:]:
            text1 = kmer1[0] + text1
            text2 = kmer2[0] + text2
        elif text1[-k+1:] == kmer1[:-1] and text2[-k+1:] == kmer2[:-1]:
            text1 = text1 + kmer1[-1]
            text2 = text2 + kmer2[-1]
        else:
            paired_kmers.append(paired_kmer)
            
    return text1 + text2[-k-distance:]
        

if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''4 2
# GAGA|TTGA
# TCGT|GATG
# CGTG|ATGT
# TGGT|TGAG
# GTGA|TGTT
# GTGG|GTGA
# TGAG|GTTG
# GGTC|GAGA
# GTCG|AGAT'''

    integers, paired_kmers_str = data.split('\n', 1)
    k, d = tuple(map(int, integers.split()))
    paired_kmers_str = paired_kmers_str.split('\n')
    
    paired_kmers = read_paired_kmers(paired_kmers_str)
    text = reconstruct_string_from_paired_kmers(paired_kmers, d)

    with open(get_output_path(__file__), "w") as f:
        print(text)
        print(text, file=f)
