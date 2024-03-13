from util import get_data, get_output_path
from Bio import SeqIO
import math

data = get_data(__file__)
# data = '''20 90
# @Rosalind_0049_1
# GCAGAGACCAGTAGATGTGTTTGCGGACGGTCGGGCTCCATGTGACACAG
# +
# FD@@;C<AI?4BA:=>C<G=:AE=><A??>764A8B797@A:58:527+,
# @Rosalind_0049_2
# AATGGGGGGGGGAGACAAAATACGGCTAAGGCAGGGGTCCTTGATGTCAT
# +
# 1<<65:793967<4:92568-34:.>1;2752)24')*15;1,.3*3+*!
# @Rosalind_0049_3
# ACCCCATACGGCGAGCGTCAGCATCTGATATCCTCTTTCAATCCTAGCTA
# +
# B:EI>JDB5=>DA?E6B@@CA?C;=;@@C:6D:3=@49;@87;::;;?8+'''

threshold, fasta = data.split('\n', 1)
threshold, percentage = map(float, threshold.split())

with open(get_output_path(__file__), 'w') as f:
  f.write(fasta)

fastaq = SeqIO.parse(get_output_path(__file__), "fastq")

n_passed_threshold = 0
for record in fastaq:
  phred_quality = record.letter_annotations["phred_quality"]
  average_quality = sum(phred_quality) / len(phred_quality)
  sorted_phred_qualify = sorted(phred_quality, reverse=True)
  index = math.ceil(len(phred_quality) * percentage / 100)-1
  
  if sorted_phred_qualify[index] >= threshold:
    n_passed_threshold += 1

print(n_passed_threshold)