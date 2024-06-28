from util import get_data
import re

data = get_data(__file__)
# data = '''>Rosalind_7142
# PFTADSMDTSNMAQCRVEDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFVYMMGQ
# FYMTKYNHGYAPARRKRFMCQTFFILTFMHFCFRRAHSMVEWCPLTTVSQFDCTPCAIFE
# WGFMMEFPCFRKQMHHQSYPPQNGLMNFNMTISWYQMKRQHICHMWAEVGILPVPMPFNM
# SYQIWEKGMSMGCENNQKDNEVMIMCWTSDIKKDGPEIWWMYNLPHYLTATRIGLRLALY
# >Rosalind_4494
# VPHRVNREGFPVLDNTFHEQEHWWKEMHVYLDALCHCPEYLDGEKVYFNLYKQQISCERY
# PIDHPSQEIGFGGKQHFTRTEFHTFKADWTWFWCEPTMQAQEIKIFDEQGTSKLRYWADF
# QRMCEVPSGGCVGFEDSQYYENQWQREEYQCGRIKSFNKQYEHDLWWCWIPVHKKPHSFL
# KTWSPAAGHRGWQFDHNFFSTKCSCIMSNCCQPPQQCGQYLTSVCWCCPEYEYVTKREEM
# >Rosalind_3636
# ETCYVSQLAYCRGPLLMNDGGYGPLLMNDGGYTISWYQAEEAFPLRWIFMMFWIDGHSCF
# NKESPMLVTQHALRGNFWDMDTCFMPNTLNQLPVRIVEFAKELIKKEFCMNWICAPDPMA
# GNSQFIHCKNCFHNCFRQVGMDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFQMM
# GHQDWGTQTFSCMHWVGWMGWVDCNYDARAHPEFYTIREYADITWYSDTSSNFRGRIGQN'''

fastas = data.split('>')[1:]
fastas = list(map(lambda x: x.split('\n', 1)[-1].replace('\n', ''), fastas))

def find_motifs(fastas, min_length=3):
  motifs = []
  motif = ''
  start_index = 0

  for i in range(1, len(fastas[0]) - 1):
    span = fastas[0][start_index:i]

    shared = True
    for fasta in fastas[1:]:
      if span not in fasta:
        shared = False
        start_index = i - 1
        break

    if shared:
      motif = span
    elif len(motif) > min_length:
      motifs.append(motif)
      motif = ''

  return motifs


def merge_motifs(motifs, fastas, min_length_missmatch=3):
  merged = []

  while len(motifs) > 1:
    motif1 = re.compile(motifs[0])
    motif2 = re.compile(motifs[1])
    
    can_connect = True
    for fasta in fastas:
      motif1_end = motif1.search(fasta).span()[1]
      motif2_start = motif2.search(fasta).span()[0]
      
      if motif2_start - motif1_end > min_length_missmatch:
        can_connect = False
        break

    if can_connect:
      mismatches = []
      for fasta in fastas:
        motif1_end = motif1.search(fasta).span()[1]
        motif2_start = motif2.search(fasta).span()[0]

        mismatch = fasta[motif1_end : motif2_start]
        mismatches.append(mismatch)

      denotes = []
      for j in range(len(mismatches[0])):
        denote = set()
        for mismatch in mismatches:
          denote.add(mismatch[j])
        denotes.append(f'[{"".join(denote)}]')

      merged.append(motifs.pop(0) + ''.join(denotes) + motifs.pop(0))
    else:
      merged.append(motifs.pop(0))

  return merged + motifs


def get_longest_motif(fastas, min_length=3, min_length_missmatch=3):
  motifs = find_motifs(fastas, min_length)
  len_motifs = len(motifs)
  new_len_motifs = 0

  while len_motifs != new_len_motifs:
    len_motifs = len(motifs)
    motifs = merge_motifs(motifs, fastas, min_length_missmatch)
    new_len_motifs = len(motifs)

  return max(motifs, key=lambda x: len(x))


motif = get_longest_motif(fastas)
print(motif)
