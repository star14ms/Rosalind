from util import get_data, get_output_path
from Bio import SeqIO

data = get_data(__file__)
# data = '''28
# @Rosalind_0041
# GGCCGGTCTATTTACGTTCTCACCCGACGTGACGTACGGTCC
# +
# 6.3536354;.151<211/0?::6/-2051)-*"40/.,+%)
# @Rosalind_0041
# TCGTATGCGTAGCACTTGGTACAGGAAGTGAACATCCAGGAT
# +
# AH@FGGGJ<GB<<9:GD=D@GG9=?A@DC=;:?>839/4856
# @Rosalind_0041
# ATTCGGTAATTGGCGTGAATCTGTTCTGACTGATAGAGACAA
# +
# @DJEJEA?JHJ@8?F?IA3=;8@C95=;=?;>D/:;74792.'''

threshold, fasta = data.split('\n', 1)
threshold = int(threshold)

with open(get_output_path(__file__), 'w') as f:
  f.write(fasta)

fastaq = SeqIO.parse(get_output_path(__file__), "fastq")

n_below_threshold = 0
for record in fastaq:
  phred_quality = record.letter_annotations["phred_quality"]
  average_quality = sum(phred_quality) / len(phred_quality)
  if average_quality < threshold:
    n_below_threshold += 1

print(n_below_threshold)
