from util import get_data, get_output_path

data = get_data(__file__)
# data = '''>Rosalind_87
# CAGCATGGTATCACAGCAGAG'''
dna = data.split('\n', 1)[1].replace('\n', '')


# find the motif that is a prefix
failure_array = [0] * len(dna)
first_prefix = dna[0]
queue = []

for i in range(1, len(dna)):
  if dna[i] == first_prefix:
    failure_array[i] = 1
    queue.append(i)

  for j in range(len(queue)-1, -1, -1):
    if dna[i-queue[j]] == dna[i]:
      failure_array[i] = i-queue[j]+1
    else:
      queue.pop(j)


print(' '.join(map(str, failure_array)))

with open(get_output_path(__file__), 'w') as output_data:
  output_data.write(' '.join(map(str, failure_array)))