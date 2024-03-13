### hard to install
from util import get_data, get_output_path
from Bio.Align.Applications import ClustalwCommandline
import os

data = get_data(__file__)
# data = '''>Rosalind_18
# GACATGTTTGTTTGCCTTAAACTCGTGGCGGCCTAGCCGTAAGTTAAG
# >Rosalind_23
# ACTCATGTTTGTTTGCCTTAAACTCTTGGCGGCTTAGCCGTAACTTAAG
# >Rosalind_51
# TCCTATGTTTGTTTGCCTCAAACTCTTGGCGGCCTAGCCGTAAGGTAAG
# >Rosalind_7
# CACGTCTGTTCGCCTAAAACTTTGATTGCCGGCCTACGCTAGTTAGTTA
# >Rosalind_28
# GGGGTCATGGCTGTTTGCCTTAAACCCTTGGCGGCCTAGCCGTAATGTTT'''

fastas = data.split('>')[1:]

with open(get_output_path(__file__), 'w') as f:
  for i, fasta in enumerate(fastas):
    f.write('>' + fasta)

# install Clustal Omega and Argtable (argtable: required for MacOS)
# http://www.clustal.org/omega/
# brew install argtable and use their path for installation of clustal omega
# https://www.biostars.org/p/128261/#128315 
clustalw = "/usr/local/bin/clustalo" 
clustalw_cline = ClustalwCommandline(
  clustalw, 
  infile=get_output_path(__file__),
  outfile=get_output_path(__file__, 'aln')
)
assert os.path.isfile(clustalw), "ClustalW executable missing" 
stdout, stderr = clustalw_cline()

print(stdout)