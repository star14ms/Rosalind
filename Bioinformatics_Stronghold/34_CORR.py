from util import get_data, get_output_path
from Bio.Seq import Seq

data = get_data(__file__)
# data = '''>Rosalind_52
# TCATC
# >Rosalind_44
# TTCAT
# >Rosalind_68
# TCATC
# >Rosalind_28
# TGAAA
# >Rosalind_95
# GAGGA
# >Rosalind_66
# TTTCA
# >Rosalind_33
# ATCAA
# >Rosalind_21
# TTGAT
# >Rosalind_18
# TTTCC'''

fastas = data.split('>')[1:]
fastas = list(map(lambda x: x.split('\n')[1], fastas))

reads = []
reads_shown_twice = []

for fasta in fastas:
  fasta_reverse_complement = Seq(fasta).reverse_complement()

  if fasta not in reads and fasta_reverse_complement not in reads:
    reads.append(fasta)
  else:
    reads_shown_twice.append(fasta)

f = open(get_output_path(__file__), 'w')


for fasta in fastas:
  fasta_reverse_complement = Seq(fasta).reverse_complement()
  
  if fasta not in reads_shown_twice and fasta_reverse_complement not in reads_shown_twice:

    for read in reads_shown_twice:
      single_error_index = None
      read_reverse_complement = Seq(read).reverse_complement()

      for i in range(len(read)):
        if fasta[i] != read[i]:
          if single_error_index is None:
            single_error_index = i
          else:
            single_error_index = None
            break
          
      if single_error_index is not None:
        f.write(fasta + '->' + read + '\n')
        print(fasta, '->', read)
        break
      
      for i in range(len(read)):
        if fasta[i] != read_reverse_complement[i]:
          if single_error_index is None:
            single_error_index = i
          else:
            single_error_index = None
            break

      if single_error_index is not None:
        f.write(fasta + '->' + read_reverse_complement + '\n')
        print(fasta, '->', read_reverse_complement)
        break
  

f.close()