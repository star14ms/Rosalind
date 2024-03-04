from util import get_data

data = get_data(__file__)

fasta = data.split('>')
dna, subsequence = [x.split('\n', 1)[1].replace('\n', '') for x in fasta if x]

subsequence_index = []

for i in range(len(dna)):
  if dna[i] == subsequence[len(subsequence_index)]:
    subsequence_index += [i+1]
    
  if len(subsequence_index) == len(subsequence):
    break
    
print(*subsequence_index)