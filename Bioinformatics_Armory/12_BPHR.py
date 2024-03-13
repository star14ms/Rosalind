from util import get_data, get_output_path
from Bio import SeqIO
import numpy as np

data = get_data(__file__)
# data = '''26
# @Rosalind_0029
# GCCCCAGGGAACCCTCCGACCGAGGATCGT
# +
# >?F?@6<C<HF?<85486B;85:8488/2/
# @Rosalind_0029
# TGTGATGGCTCTCTGAATGGTTCAGGCAGT
# +
# @J@H@>B9:B;<D==:<;:,<::?463-,,
# @Rosalind_0029
# CACTCTTACTCCCTAGCCGAACTCCTTTTT
# +
# =88;99637@5,4664-65)/?4-2+)$)$
# @Rosalind_0029
# GATTATGATATCAGTTGGCTCCGAGAGCGT
# +
# <@BGE@8C9=B9:B<>>>7?B>7:02+33.'''

threshold, fasta = data.split('\n', 1)
threshold = float(threshold)

with open(get_output_path(__file__), 'w') as f:
  f.write(fasta)

fastaq = SeqIO.parse(get_output_path(__file__), "fastq")

sum_of_n_below_threshold = 0
n_fastaq = 0

phred_qualities = []
for record in fastaq:
  phred_quality = record.letter_annotations["phred_quality"]
  
  phred_qualities.append(phred_quality)


# Convert the list of quality scores into a NumPy array for easier manipulation
quality_array = np.array(phred_qualities)

# Calculate the mean quality score for each position
mean_qualities = quality_array.mean(axis=0)

# Count the number of positions where the mean quality score falls below the threshold
below_threshold_count = np.sum(mean_qualities < threshold)

print(below_threshold_count)
