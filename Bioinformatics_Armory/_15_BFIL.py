from util import get_data, get_output_path
from Bio import SeqIO

data = get_data(__file__)
# data = '''20
# @Rosalind_0049
# GCAGAGACCAGTAGATGTGTTTGCGGACGGTCGGGCTCCATGTGACACAG
# +
# FD@@;C<AI?4BA:=>C<G=:AE=><A??>764A8B797@A:58:527+,
# @Rosalind_0049
# AATGGGGGGGGGAGACAAAATACGGCTAAGGCAGGGGTCCTTGATGTCAT
# +
# 1<<65:793967<4:92568-34:.>1;2752)24')*15;1,.3*3+*!
# @Rosalind_0049
# ACCCCATACGGCGAGCGTCAGCATCTGATATCCTCTTTCAATCCTAGCTA
# +
# B:EI>JDB5=>DA?E6B@@CA?C;=;@@C:6D:3=@49;@87;::;;?8+'''

threshold, fasta = data.split('\n', 1)
threshold = float(threshold)
print(threshold)

with open(get_output_path(__file__), 'w') as f:
  f.write(fasta)

fastaqs = SeqIO.parse(get_output_path(__file__), "fastq")

new_fastaqs = []

for fastaq in fastaqs:
  phred_quality = fastaq.letter_annotations["phred_quality"]
  
  # trim the both end of the sequence to remove low quality base
  
  # trim the left end
  l = 0
  for i in range(len(phred_quality)):
    if phred_quality[i] < threshold:
      l += 1
    else:
      break
    
  # trim the right end
  r = len(phred_quality)
  for i in range(len(phred_quality) - 1, -1, -1):
    if phred_quality[i] < threshold:
      r -= 1
    else:
      break

  new_fastaqs.append(fastaq[l:r].format("fastq"))


with open(get_output_path(__file__), 'w') as f:
  for fastaq in new_fastaqs:
    f.write(fastaq)
